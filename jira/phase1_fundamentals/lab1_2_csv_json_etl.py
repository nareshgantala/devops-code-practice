"""
=============================================================================
LAB 1.2 — CSV/JSON ETL for Jira Bulk Operations
=============================================================================

SCENARIO:
    You're a Jira Admin and need to create 100 tickets from a spreadsheet.
    Instead of clicking through the UI one-by-one, you'll:
      1. Read a CSV file containing ticket data
      2. Validate each row (reject bad data)
      3. Transform valid rows into Jira REST API JSON payloads
      4. Save the payloads to a file (ready to POST to Jira)
      5. Log invalid rows to an error file

    ETL = Extract (CSV) → Transform (validate + format) → Load (JSON output)

    The sample CSV is in: data/bulk_issues.csv

WHY THIS MATTERS:
    - Jira Admins frequently bulk-create/update tickets during migrations
    - The Jira REST API expects a specific JSON payload format
    - Production scripts MUST handle bad data without crashing

PYTHON CONCEPTS YOU'LL PRACTICE:
    1. csv.DictReader       — Read CSV rows as dictionaries
    2. json.dumps()         — Convert Python dict to JSON string
    3. json.dump()          — Write Python dict to a JSON file
    4. try/except           — Handle errors without crashing
    5. open("file", "w")    — Write to files
    6. string methods       — .strip() removes whitespace
    7. enumerate()          — Loop with index: (1, row1), (2, row2)...
    8. os.makedirs()        — Create directories safely

CSV FILE FORMAT (bulk_issues.csv):
    Summary,Description,IssueType,Priority,Component
    "Set up Terraform...", "Configure S3...", Story, High, Infrastructure
    ...
    Note: Some rows have MISSING fields — your code should catch these!

JIRA API PAYLOAD FORMAT (what you need to build):
    {
        "fields": {
            "project": {"key": "KAN"},
            "summary": "Ticket title here",
            "description": {
                "type": "doc",
                "version": 1,
                "content": [
                    {
                        "type": "paragraph",
                        "content": [
                            {"type": "text", "text": "Description text here"}
                        ]
                    }
                ]
            },
            "issuetype": {"name": "Story"},
            "priority": {"name": "High"},
            "components": [{"name": "Infrastructure"}]
        }
    }
=============================================================================
"""

import csv
import json
import os
from datetime import datetime

# SETUP: Define file paths
script_dir = os.path.dirname(__file__)
csv_file = os.path.join(script_dir, "data", "bulk_issues.csv")
output_dir = os.path.join(script_dir, "output")
payload_file = os.path.join(output_dir, "jira_payloads.json")
error_file = os.path.join(output_dir, "errors.log")

# Create output directory
os.makedirs(output_dir, exist_ok=True)

PROJECT_KEY = "KAN"     # Your Jira project key

# ===========================================================================
# TASK 1: Read the CSV file using csv.DictReader
# ===========================================================================
# Read all rows from the CSV file into a list.
# Print how many rows were read and show the first row.
#
# Hints:
#   with open(csv_file, "r") as f:
#       reader = csv.DictReader(f)
#       for row in reader:
#           rows.append(row)
#   print(json.dumps(rows[0], indent=2))  # Pretty-print first row

# YOUR CODE HERE:


# ===========================================================================
# TASK 2: Validate each row
# ===========================================================================
# Rules:
#   - Summary MUST exist (not empty after .strip())
#   - Priority MUST exist
#   - IssueType MUST exist
#
# Separate rows into valid_rows and invalid_rows lists.
# For invalid rows, record the row number and what's wrong.
#
# Hints:
#   for index, row in enumerate(rows, start=1):
#       summary = row.get("Summary", "").strip()
#       if not summary:   # empty string is falsy in Python
#           errors.append("Missing Summary")

# YOUR CODE HERE:


# ===========================================================================
# TASK 3: Transform valid rows into Jira API payloads
# ===========================================================================
# For each valid row, build a payload dict matching the JIRA API FORMAT
# shown above in the docstring.
# Don't forget: description uses Atlassian Document Format (ADF).
# Only add "components" if the Component column is not empty.
#
# Hints:
#   description_adf = {
#       "type": "doc", "version": 1,
#       "content": [{"type": "paragraph",
#                     "content": [{"type": "text", "text": row["Description"]}]}]
#   }

# YOUR CODE HERE:


# ===========================================================================
# TASK 4: Save valid payloads to a JSON file
# ===========================================================================
# Write the list of payloads to jira_payloads.json
#
# Hints:
#   with open(payload_file, "w") as f:
#       json.dump(payloads, f, indent=2)
#
# Remember: json.dump() → file, json.dumps() → string

# YOUR CODE HERE:


# ===========================================================================
# TASK 5: Save invalid rows to an error log
# ===========================================================================
# Write each invalid row with its row number and error reasons.
# Include a timestamp at the top of the file.
#
# Hints:
#   f.write(f"Row {entry['row_number']}: {', '.join(entry['errors'])}\n")

# YOUR CODE HERE:


# ===========================================================================
# TASK 6: Print a summary report
# ===========================================================================
# Show: total rows, valid count, invalid count, output file paths
# Bonus: count how many of each IssueType were created
#
# YOUR CODE HERE:


print("\n✅ Lab 1.2 Complete!")
