"""
=============================================================================
LAB 1.1 — Nested Dict & List Traversal (Jira Payload Parsing)
=============================================================================

SCENARIO:
    You've just called the Jira REST API endpoint:
        GET /rest/api/3/search?jql=project=KAN

    The API returned a JSON response with nested dictionaries and lists.
    Your job: parse this response and extract useful information.

    The mock response is in: data/mock_jira_response.json

WHY THIS MATTERS:
    Every Jira/AWS/Azure API returns JSON like this. If you can parse nested
    dicts and lists confidently, you can automate ANYTHING.

PYTHON CONCEPTS YOU'LL PRACTICE:
    1. json.load()         — Load JSON from a file into Python dict/list
    2. dict["key"]         — Access a dictionary value (crashes if key missing)
    3. dict.get("key")     — Safe access (returns None if key missing)
    4. for item in list    — Loop through a list
    5. list comprehension  — One-line list filtering
    6. set()               — Collection of unique values (no duplicates)
    7. f-strings           — f"text {variable}" for clean output formatting
    8. if/elif/else        — Conditional logic

RUN:
    python jira/phase1_fundamentals/lab1_1_nested_dict_parsing.py

DATA STRUCTURE REFERENCE (what the JSON looks like):
    {
        "total": 5,
        "startAt": 0,
        "maxResults": 50,
        "issues": [
            {
                "key": "KAN-1",
                "fields": {
                    "summary": "Set up CI/CD pipeline...",
                    "status": { "name": "In Progress" },
                    "assignee": { "displayName": "Naresh Gantala" } or null,
                    "priority": { "name": "High" },
                    "project": { "key": "KAN" },
                    "customfield_10014": "KAN-100" or null,
                    "labels": ["devops", "ci-cd"],
                    "components": [{ "name": "Infrastructure" }]
                }
            },
            ...more issues...
        ]
    }
=============================================================================
"""

import json
import os

# SETUP: Load the mock Jira response
# Hint: os.path.dirname(__file__) gets the folder where THIS script lives
# Hint: os.path.join() safely builds file paths across OS types

script_dir = os.path.dirname(__file__)
data_file = os.path.join(script_dir, "data", "mock_jira_response.json")

# ===========================================================================
# TASK 1: Load JSON and print top-level metadata
# ===========================================================================
# Open the JSON file and load it into a Python dictionary.
# Print: total issues, startAt, maxResults
#
# Hints:
#   with open(filepath, "r") as f:
#       data = json.load(f)
#   print(f"Total: {data['total']}")

# YOUR CODE HERE:


# ===========================================================================
# TASK 2: Loop through issues and print a formatted table
# ===========================================================================
# Print each issue's: Key, Status, Assignee, Summary
# Handle the case where assignee is None (null) — print "Unassigned"
#
# Hints:
#   issues = data["issues"]
#   for issue in issues:
#       key = issue["key"]
#       status = issue["fields"]["status"]["name"]
#       assignee_data = issue["fields"]["assignee"]  # Could be None!
#       if assignee_data is not None:
#           name = assignee_data["displayName"]

# YOUR CODE HERE:


# ===========================================================================
# TASK 3: Find all UNASSIGNED issues
# ===========================================================================
# Collect all issue keys where assignee is None.
# First do it with a for loop, then try a list comprehension.
#
# Hints:
#   Loop version:
#       unassigned = []
#       for issue in issues:
#           if issue["fields"]["assignee"] is None:
#               unassigned.append(issue["key"])
#
#   List comprehension version:
#       unassigned = [i["key"] for i in issues if i["fields"]["assignee"] is None]

# YOUR CODE HERE:


# ===========================================================================
# TASK 4: Extract unique project keys using set()
# ===========================================================================
# Some issues are in "KAN", some in "OPS". Get unique project keys.
#
# Hints:
#   set() removes duplicates automatically
#   Set comprehension: {issue["fields"]["project"]["key"] for issue in issues}

# YOUR CODE HERE:


# ===========================================================================
# TASK 5: Find issues by status (e.g., all "To Do" issues)
# ===========================================================================
# Use a list comprehension to filter issues by status name.
#
# YOUR CODE HERE:


# ===========================================================================
# TASK 6: Count issues per status (build a dictionary)
# ===========================================================================
# Build a dict like: {"To Do": 2, "In Progress": 2, "Done": 1}
#
# Hints:
#   counts = {}
#   for issue in issues:
#       status = issue["fields"]["status"]["name"]
#       counts[status] = counts.get(status, 0) + 1

# YOUR CODE HERE:


# ===========================================================================
# TASK 7: Safely access custom fields (Epic Link)
# ===========================================================================
# customfield_10014 is the Epic Link. It can be None.
# Use .get() to access it safely.
#
# YOUR CODE HERE:


# ===========================================================================
# TASK 8: Find issues with a specific label (e.g., "aws")
# ===========================================================================
# labels is a list of strings. Use the `in` keyword to check membership.
#
# Hints:
#   labels = issue["fields"].get("labels", [])
#   if "aws" in labels:
#       ...

# YOUR CODE HERE:


print("\n✅ Lab 1.1 Complete!")
