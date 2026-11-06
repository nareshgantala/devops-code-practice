import html
import html
import os
import requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# 1. Authentication & Configuration
DOMAIN = (os.getenv("CONFLUENCE_DOMAIN") or os.getenv("JIRA_DOMAIN") or "").rstrip("/")
EMAIL = os.getenv("CONFLUENCE_EMAIL") or os.getenv("JIRA_EMAIL")
API_TOKEN = os.getenv("API_TOKEN")

# Organization Admin API details (for resolving Group ID -> Group Name)
ORG_ID = os.getenv("ORG_ID")
ORG_API_KEY = os.getenv("ORG_API_KEY") or API_TOKEN

# Target Space ID where the Confluence report page will be created
TARGET_SPACE_ID = os.getenv("TARGET_SPACE_ID")
PAGE_TITLE = os.getenv("PAGE_TITLE", "Confluence Space Roles Report")

auth = HTTPBasicAuth(EMAIL, API_TOKEN)
headers = {
    "Accept": "application/json",
    "Content-Type": "application/json",
}

# Caches to avoid redundant API calls for the same role, user, or group ID
role_cache = {}
group_cache = {}
user_cache = {}


def get_all_spaces():
    """
    2. Fetch all non-personal Confluence spaces using REST API v2:
    https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-space/#api-spaces-get
    """
    spaces = []
    url = f"{DOMAIN}/wiki/api/v2/spaces"

    while url:
        response = requests.get(url, headers=headers, auth=auth)
        response.raise_for_status()
        data = response.json()

        # Skip personal/user spaces (where type == 'personal')
        for space in data.get("results", []):
            if space.get("type") != "personal":
                spaces.append(space)

        # Handle cursor pagination if there are more spaces
        next_link = data.get("_links", {}).get("next")
        url = f"{DOMAIN}{next_link}" if next_link else None

    return spaces


def get_space_role_assignments(space_id):
    """
    3. Fetch users/groups and role IDs associated with a space:
    https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-space-roles/#api-spaces-id-role-assignments-get
    """
    assignments = []
    url = f"{DOMAIN}/wiki/api/v2/spaces/{space_id}/role-assignments"

    while url:
        response = requests.get(url, headers=headers, auth=auth)
        if response.status_code == 404:
            # Space roles might not be enabled or accessible for this specific space
            break
        response.raise_for_status()
        data = response.json()

        assignments.extend(data.get("results", []))

        next_link = data.get("_links", {}).get("next")
        url = f"{DOMAIN}{next_link}" if next_link else None

    return assignments


def get_role_name(role_id):
    """
    4. Fetch space role details by role ID:
    https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-space-roles/#api-space-roles-id-get
    """
    if not role_id:
        return "Unassigned"

    if role_id in role_cache:
        return role_cache[role_id]

    url = f"{DOMAIN}/wiki/api/v2/space-roles/{role_id}"
    response = requests.get(url, headers=headers, auth=auth)

    if response.status_code == 200:
        role_name = response.json().get("name", role_id)
    else:
        role_name = role_id

    role_cache[role_id] = role_name
    return role_name


def get_group_name_from_org(group_id):
    """
    Resolve Group Name from Group ID using Atlassian Admin Organization Groups API:
    https://developer.atlassian.com/cloud/admin/organization/rest/api-group-groups/#api-group-groups
    POST https://api.atlassian.com/admin/v1/orgs/{orgId}/groups/search
    """
    if group_id in group_cache:
        return group_cache[group_id]

    group_name = group_id

    # Use Organization REST API if ORG_ID is provided
    if ORG_ID and ORG_API_KEY:
        org_url = f"https://api.atlassian.com/admin/v1/orgs/{ORG_ID}/groups/search"
        org_headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "Authorization": f"Bearer {ORG_API_KEY}",
        }
        payload = {"groupIds": [group_id]}
        response = requests.post(org_url, headers=org_headers, json=payload)

        if response.status_code == 200:
            groups_data = response.json().get("data", [])
            if groups_data:
                group_obj = groups_data[0]
                # Support both direct 'name' and JSON:API 'attributes.name'
                group_name = (
                    group_obj.get("name")
                    or group_obj.get("attributes", {}).get("name")
                    or group_id
                )
                group_cache[group_id] = group_name
                return group_name

    # Fallback: Confluence Group by ID endpoint if Org API is not configured
    fallback_url = f"{DOMAIN}/wiki/rest/api/group/by-id"
    response = requests.get(
        fallback_url, headers=headers, params={"id": group_id}, auth=auth
    )
    if response.status_code == 200:
        group_name = response.json().get("name", group_id)

    group_cache[group_id] = group_name
    return group_name


def get_user_display_name(account_id):
    """
    Resolve User Display Name from Atlassian accountId.
    """
    if account_id in user_cache:
        return user_cache[account_id]

    url = f"{DOMAIN}/wiki/rest/api/user"
    response = requests.get(
        url, headers=headers, params={"accountId": account_id}, auth=auth
    )

    if response.status_code == 200:
        user_name = response.json().get("displayName", account_id)
    else:
        user_name = account_id

    user_cache[account_id] = user_name
    return user_name


def resolve_principal_name(principal):
    """
    Determine whether the principal is a USER, GROUP, or ACCESS_CLASS and resolve its name.
    """
    principal_type = principal.get("principalType")
    principal_id = principal.get("principalId")

    if principal_type == "GROUP":
        return f"{get_group_name_from_org(principal_id)} (Group)"
    elif principal_type == "USER":
        return f"{get_user_display_name(principal_id)} (User)"
    else:
        return f"{principal_id} ({principal_type})"


def build_confluence_table_html(rows):
    """
    Build Confluence Storage Format HTML table with 4 columns:
    Serial No | Space Name | User/Group Name | Space Role
    Uses rowspan to merge 'Serial No' and 'Space Name' across all users/groups in the same space.
    """
    # Count how many rows belong to each space so we can set rowspan
    space_counts = {}
    for row in rows:
        space_name = row["space_name"]
        space_counts[space_name] = space_counts.get(space_name, 0) + 1

    table_rows_html = ""
    rendered_spaces = set()
    space_serial_no = 1

    for row in rows:
        space_name = row["space_name"]
        table_rows_html += "<tr>"

        # Only render Serial No and Space Name on the first row for that space, spanning all its rows
        if space_name not in rendered_spaces:
            rowspan = space_counts[space_name]
            table_rows_html += f'<td rowspan="{rowspan}">{space_serial_no}</td>'
            table_rows_html += (
                f'<td rowspan="{rowspan}">{html.escape(str(space_name))}</td>'
            )
            rendered_spaces.add(space_name)
            space_serial_no += 1

        table_rows_html += f"<td>{html.escape(str(row['principal_name']))}</td>"
        table_rows_html += f"<td>{html.escape(str(row['role_name']))}</td>"
        table_rows_html += "</tr>"

    table_html = (
        "<table>"
        "<thead>"
        "<tr>"
        "<th>Serial No</th>"
        "<th>Space Name</th>"
        "<th>User / Group Name</th>"
        "<th>Space Role</th>"
        "</tr>"
        "</thead>"
        "<tbody>"
        f"{table_rows_html}"
        "</tbody>"
        "</table>"
    )
    return table_html


def create_confluence_page(space_id, title, body_html):
    """
    Create (or update if it already exists) a Confluence page using REST API v2:
    POST /wiki/api/v2/pages
    """
    # Check if a page with this title already exists in the target space
    search_url = f"{DOMAIN}/wiki/api/v2/spaces/{space_id}/pages"
    search_resp = requests.get(
        search_url, headers=headers, params={"title": title}, auth=auth
    )
    if search_resp.status_code == 200:
        existing_pages = search_resp.json().get("results", [])
        if existing_pages:
            page_id = existing_pages[0].get("id")
            current_version = existing_pages[0].get("version", {}).get("number", 1)
            update_url = f"{DOMAIN}/wiki/api/v2/pages/{page_id}"
            update_payload = {
                "id": str(page_id),
                "status": "current",
                "title": title,
                "body": {
                    "representation": "storage",
                    "value": body_html,
                },
                "version": {
                    "number": current_version + 1,
                    "message": "Updated space roles report",
                },
            }
            update_resp = requests.put(
                update_url, headers=headers, json=update_payload, auth=auth
            )
            if not update_resp.ok:
                print(f"Error updating page: {update_resp.text}")
            update_resp.raise_for_status()
            return update_resp.json()

    url = f"{DOMAIN}/wiki/api/v2/pages"
    payload = {
        "spaceId": str(space_id),
        "status": "current",
        "title": title,
        "body": {
            "representation": "storage",
            "value": body_html,
        },
    }

    response = requests.post(url, headers=headers, json=payload, auth=auth)
    if not response.ok:
        print(f"Error creating page: {response.text}")
    response.raise_for_status()
    return response.json()


def main():
    if not DOMAIN or not EMAIL or not API_TOKEN:
        raise ValueError(
            "Missing required credentials. Please set CONFLUENCE_DOMAIN (or JIRA_DOMAIN), "
            "CONFLUENCE_EMAIL (or JIRA_EMAIL), and API_TOKEN in your .env file."
        )

    print("Fetching Confluence spaces...")
    spaces = get_all_spaces()
    print(f"Found {len(spaces)} spaces.")

    if not spaces:
        print("No spaces found.")
        return

    table_rows = []
    serial_no = 1

    for space in spaces:
        space_id = space.get("id")
        space_name = space.get("name")
        print(f"Fetching role assignments for space: {space_name} (ID: {space_id})...")

        assignments = get_space_role_assignments(space_id)

        for assignment in assignments:
            principal = assignment.get("principal", {})
            role_id = assignment.get("roleId")

            principal_name = resolve_principal_name(principal)
            role_name = get_role_name(role_id)

            table_rows.append(
                {
                    "serial_no": serial_no,
                    "space_name": space_name,
                    "principal_name": principal_name,
                    "role_name": role_name,
                }
            )
            serial_no += 1

    # Choose target space to publish the page (use TARGET_SPACE_ID if valid, otherwise first space found)
    valid_space_ids = {str(s.get("id")) for s in spaces}
    if TARGET_SPACE_ID and str(TARGET_SPACE_ID) in valid_space_ids:
        target_space_id = str(TARGET_SPACE_ID)
    else:
        target_space_id = str(spaces[0].get("id"))

    print(f"Generating Confluence page '{PAGE_TITLE}' in space ID {target_space_id}...")
    table_html = build_confluence_table_html(table_rows)
    created_page = create_confluence_page(target_space_id, PAGE_TITLE, table_html)

    webui_link = created_page.get("_links", {}).get("webui", "")
    print(f"Confluence page created successfully! Page ID: {created_page.get('id')}")
    if webui_link:
        print(f"Page URL: {DOMAIN}/wiki{webui_link}")


if __name__ == "__main__":
    main()

