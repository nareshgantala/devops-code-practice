# Confluence Space Roles Report Automation (`confluence_space_roles.py`)

This script connects to **Confluence Cloud REST API v2** and the **Atlassian Administration Organization API** to audit all Confluence spaces, fetch the users/groups assigned to each space along with their space roles, and publish (or update) a Confluence report page containing a formatted 4-column table.

---

## Table Columns Generated
| Column | Description |
| :--- | :--- |
| **Serial No** | Merged per space (`rowspan`) |
| **Space Name** | Confluence Space Name, merged across all assigned users/groups (`rowspan`) |
| **User / Group Name** | Display name of the User, Group, or Access Class (`USER`, `GROUP`, `ACCESS_CLASS`) |
| **Space Role** | Assigned Role Name (e.g., `Admin`, `Collaborator`, `Viewer`) |

---

## REST APIs Used
1. **Get Spaces (Confluence REST API v2)**  
   `GET https://<your-domain>.atlassian.net/wiki/api/v2/spaces`  
   [Documentation](https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-space/#api-group-space)
2. **Get Space Role Assignments (Confluence REST API v2)**  
   `GET https://<your-domain>.atlassian.net/wiki/api/v2/spaces/{id}/role-assignments`  
   [Documentation](https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-space-roles/#api-spaces-id-role-assignments-get)
3. **Get Space Role by ID (Confluence REST API v2)**  
   `GET https://<your-domain>.atlassian.net/wiki/api/v2/space-roles/{id}`  
   [Documentation](https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-space-roles/#api-space-roles-id-get)
4. **Search Organization Groups by ID (Atlassian Admin Organization API)**  
   `POST https://api.atlassian.com/admin/v1/orgs/{orgId}/groups/search`  
   [Documentation](https://developer.atlassian.com/cloud/admin/organization/rest/api-group-groups/#api-group-groups)
5. **Create / Update Page (Confluence REST API v2)**  
   `POST https://<your-domain>.atlassian.net/wiki/api/v2/pages`  
   `PUT https://<your-domain>.atlassian.net/wiki/api/v2/pages/{id}`

---

## `.env` File Setup

Create a `.env` file in the `python/jira/` directory with the following variables:

```env
# Confluence / Jira Site Credentials
JIRA_DOMAIN="https://your-domain.atlassian.net"
JIRA_EMAIL="your-email@example.com"
API_TOKEN="your_atlassian_api_token"

# Organization Admin API Credentials (for resolving Group ID -> Group Name)
ORG_ID="your_organization_id"
ORG_API_KEY="your_org_admin_api_key"

# Target Confluence Space & Page Settings
TARGET_SPACE_ID="524292" #(The space in which new page to be created)
PAGE_TITLE="Confluence Space Roles Report"
```

---

## How to Get Each `.env` Value

### 1. `API_TOKEN` (Personal Atlassian API Token)
1. Go to [https://id.atlassian.com/manage-profile/security/api-tokens](https://id.atlassian.com/manage-profile/security/api-tokens).
2. Click **Create API token**, give it a label, and copy the generated token.

### 2. `ORG_ID` (Organization ID)
1. Log in to [https://admin.atlassian.com](https://admin.atlassian.com).
2. Select your organization.
3. Copy the UUID from the browser URL:
   ```text
   https://admin.atlassian.com/o/<YOUR_ORG_ID>/...
   ```
   *(Also shown at the top of **Settings** → **API keys**.)*

### 3. `ORG_API_KEY` (Organization Admin API Key)
1. In [https://admin.atlassian.com](https://admin.atlassian.com), go to **Settings** → **API keys**.
2. Click **Create API key** in the top right.
3. Enter a name and expiration date, then copy the key.
   *(Note: If `ORG_ID` and `ORG_API_KEY` are left empty, the script automatically falls back to Confluence's `/wiki/rest/api/group/by-id` endpoint using your personal `API_TOKEN`.)*

### 4. `TARGET_SPACE_ID` (Confluence Space ID)
- Open `https://<your-domain>.atlassian.net/wiki/api/v2/spaces` in your browser while logged in to view each space's `"id"` and `"name"`.
- If `TARGET_SPACE_ID` is omitted or invalid, the script defaults to the first space returned by the API.

---

## How to Run

From the `python/jira` directory:

```powershell
cd python/jira
python confluence_space_roles.py
```

