# Phase 1: Python Fundamentals

> **Focus**: Learn core Python concepts using real Jira/DevOps scenarios — no theoretical exercises.

These labs use **mock data** (no Jira connection required), so you can practice anywhere.

---

## Learning Objectives

After completing Phase 1, you will be able to:

- ✅ Parse nested JSON responses from Jira APIs
- ✅ Safely access dictionary keys without crashing your script
- ✅ Transform CSV data into valid Jira REST API payloads
- ✅ Handle errors gracefully with `try/except`
- ✅ Load configuration securely from environment variables
- ✅ Work with files and directories using `os` and `pathlib`
- ✅ Use Python's `logging` module instead of `print()`

---

## Labs

### Lab 1.1 — Nested Dict & List Traversal (Jira Payload Parsing)

**Scenario**: You've fetched Jira search results. Parse the nested response to extract useful information.

**Concepts**: `dict`, `list`, `.get()`, `set()`, list comprehensions, `f-strings`, `for` loops

**Run**: `python jira/phase1_fundamentals/lab1_1_nested_dict_parsing.py`

---

### Lab 1.2 — CSV/JSON ETL for Jira Bulk Operations

**Scenario**: You need to bulk-create 100 Jira tickets from a CSV file. Transform each row into a valid API payload.

**Concepts**: `csv` module, `json` module, `try/except`, file writing, data validation

**Run**: `python jira/phase1_fundamentals/lab1_2_csv_json_etl.py`

---

### Lab 1.3 — Secure Environment & File Operations

**Scenario**: Build an admin script that loads credentials securely and audits local backup files.

**Concepts**: `os`, `pathlib`, custom exceptions, `datetime`, `logging`, `sys.exit()`

**Run**: `python jira/phase1_fundamentals/lab1_3_env_file_operations.py`

---

## Data Files

| File | Purpose |
|------|---------|
| `data/mock_jira_response.json` | Realistic Jira search response with 5 issues (mixed statuses, assignees, projects) |
| `data/bulk_issues.csv` | 10 rows for bulk ticket creation (includes 3 intentionally invalid rows) |

---

## Tips

1. **Read the comments** — every lab is heavily commented to explain *why* each pattern matters
2. **Run the script first** — see the output, then read the code to understand how it works
3. **Modify and experiment** — change values, break things, fix them
4. **Check the hints** — commented-out hints at the bottom of each lab if you get stuck
