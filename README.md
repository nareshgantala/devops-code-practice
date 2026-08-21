# 🐍 DevOps Python Labs — Jira Admin & DevOps Automation

> **Goal**: Master Python by building real Jira Admin and DevOps automation scripts — not theoretical exercises.

This repository is a structured, hands-on Python lab project designed for **Senior Jira Admin** and **Senior DevOps Engineer** interview preparation.

Every lab is tied to a real-world scenario you'd encounter in production: parsing API responses, bulk-creating tickets, auditing users, handling rate limits, and integrating Jira with AWS/Azure/Kubernetes.

---

## 📋 Roadmap

| Phase | Focus Area | Labs | Status |
|-------|-----------|------|--------|
| **Phase 1** | Python Fundamentals | 1.1 – 1.3 | 🔄 In Progress |
| **Phase 2** | Jira REST API Operations | 2.1 – 2.3 | ⏳ Upcoming |
| **Phase 3** | Production-Quality Patterns | 3.1 | ⏳ Upcoming |
| **Phase 4** | DevOps & Jira Bridge Projects | 4.1 – 4.4 | ⏳ Upcoming |

### Phase 1: Python Fundamentals (You Are Here 👈)
| Lab | Title | Python Concepts |
|-----|-------|----------------|
| 1.1 | Nested Dict & List Traversal | `dict`, `list`, `.get()`, `set()`, list comprehensions, `f-strings` |
| 1.2 | CSV/JSON ETL for Bulk Operations | `csv`, `json`, `try/except`, file I/O, validation |
| 1.3 | Secure Environment & File Operations | `os`, `pathlib`, custom exceptions, `datetime`, `logging` |

### Phase 2: Core Jira Admin API
| Lab | Title | Python Concepts |
|-----|-------|----------------|
| 2.1 | Authentication, Pagination & JQL | `requests.Session()`, Basic Auth, pagination loops, generators |
| 2.2 | Issue Lifecycle & Custom Fields | HTTP POST/PUT, API endpoints, JSON payloads |
| 2.3 | User Governance & Permission Audit | User/Group APIs, CSV export, filtering |

### Phase 3: Senior-Level Production Patterns
| Lab | Title | Python Concepts |
|-----|-------|----------------|
| 3.1 | Rate Limiting & Exponential Backoff | Decorators, `time.sleep()`, `logging`, retry logic |

### Phase 4: DevOps & Jira Bridge Projects
| Lab | Title | Key Libraries |
|-----|-------|--------------|
| 4.1 | AWS Alert → JSM Incident | `boto3`, `requests`, `json` |
| 4.2 | Automated Patch Ticket Creator | `boto3`, `csv`, `requests` |
| 4.3 | K8s Pod CrashLoop Reporter | `kubernetes`, `requests`, `logging` |
| 4.4 | SSL/ACM Expiry Watchdog | `boto3`, `cryptography`, `requests` |

---

## 🚀 Setup

### Prerequisites
- Python 3.10+ installed
- A Jira Cloud instance (free tier works)
- API Token from [Atlassian API Tokens](https://id.atlassian.com/manage-profile/security/api-tokens)

### Installation

```bash
# Clone the repo
git clone <your-repo-url>
cd devops-python

# Install dependencies
pip install -r requirements.txt
```

### Environment Variables

Create a `.env` file inside the `jira/` directory:

```env
API_TOKEN = "your_jira_api_token_here"
JIRA_DOMAIN = "https://your-domain.atlassian.net"
JIRA_EMAIL = "your-email@example.com"
```

> ⚠️ **Never commit `.env` files to Git!** The `.gitignore` already excludes them.

---

## 🏃 How to Run

Each lab is a standalone Python script. Run from the project root:

```bash
# Phase 1 Labs (no Jira connection needed — uses mock data)
python jira/phase1_fundamentals/lab1_1_nested_dict_parsing.py
python jira/phase1_fundamentals/lab1_2_csv_json_etl.py
python jira/phase1_fundamentals/lab1_3_env_file_operations.py

# Phase 2+ Labs (requires Jira connection)
python jira/fetch_jira_issues.py
```

---

## 🧠 Python Concepts Cheat Sheet

### String Concatenation (used in API URL building)
```python
# The + operator joins strings together
base_url = os.getenv("JIRA_DOMAIN")           # "https://nareshjira.atlassian.net"
endpoint = "/rest/api/3/search/jql"            # API endpoint path
full_url = base_url + endpoint                 # Combined: full API URL

# f-strings — a cleaner way to build strings with variables
issue_key = "KAN-101"
url = f"{base_url}/rest/api/3/issue/{issue_key}"
```

### Safe Dictionary Access
```python
# ❌ Dangerous — crashes if key doesn't exist
name = user["displayName"]      # KeyError if user has no displayName!

# ✅ Safe — returns None (or a default) if key is missing
name = user.get("displayName")              # Returns None if missing
name = user.get("displayName", "Unknown")   # Returns "Unknown" if missing
```

### Looping Through API Responses
```python
# Jira API returns: {"issues": [{"key": "KAN-1", ...}, {"key": "KAN-2", ...}]}
for issue in data["issues"]:
    print(issue["key"])                   # "KAN-1", "KAN-2", ...
    print(issue["fields"]["summary"])     # Nested access
```

### List Comprehension (one-line filtering)
```python
# Traditional loop
unassigned = []
for issue in issues:
    if issue["fields"]["assignee"] is None:
        unassigned.append(issue["key"])

# Same thing as a list comprehension — shorter & Pythonic
unassigned = [i["key"] for i in issues if i["fields"]["assignee"] is None]
```

---

## 📁 Project Structure

```
devops-python/
├── README.md                              ← You are here
├── requirements.txt                       ← Python dependencies
├── .gitignore                             ← Files excluded from Git
│
└── jira/
    ├── .env                               ← Your Jira credentials (not committed)
    ├── fetch_jira_issues.py               ← Your first working API script
    │
    ├── phase1_fundamentals/               ← Python basics with Jira context
    │   ├── README.md
    │   ├── data/
    │   │   ├── mock_jira_response.json
    │   │   └── bulk_issues.csv
    │   ├── lab1_1_nested_dict_parsing.py
    │   ├── lab1_2_csv_json_etl.py
    │   └── lab1_3_env_file_operations.py
    │
    ├── phase2_jira_api/                   ← Jira REST API operations
    │   └── README.md
    │
    ├── phase3_production_patterns/        ← Production-quality scripting
    │   └── README.md
    │
    └── phase4_devops_bridge/              ← AWS/K8s + Jira integrations
        └── README.md
```

---

## 🎯 Interview Target

After completing all phases, you should be able to confidently say:

> *"I can write Python scripts to interact with Jira REST APIs, automate AWS/Azure operations, process JSON/CSV data, and build production-quality operational tooling with proper logging, error handling, and retry logic."*

---

## 📝 License

This project is for personal learning and interview preparation.
