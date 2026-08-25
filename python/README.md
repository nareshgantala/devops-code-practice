# 🐍 DevOps Python — Jira, AWS & Azure Automation

> **Goal**: Master Python by building real Jira Admin and DevOps automation scripts — not theoretical exercises.

A hands-on Python learning project for **Senior Jira Admin** and **Senior DevOps Engineer** interview preparation. Every script connects to a real API — Jira Cloud, AWS, or Azure.

---

## 📁 Project Structure

```
devops-python/
├── README.md                    ← You are here
├── requirements.txt             ← Python dependencies
├── LEARNING_JOURNAL.md          ← Session notes & progress
├── flashcards.md                ← Spaced repetition cards (33 cards)
├── .gitignore                   ← Files excluded from Git
│
├── jira/
│   ├── .env                     ← Jira credentials (not committed)
│   └── fetch_jira_issues.py     ← Fetch issues from Jira Cloud API
│
├── aws/
│   └── fetch_ec2_instances.py   ← Fetch EC2 instances using boto3
│
└── azure/
    └── fetch_vms.py             ← Fetch VMs using Azure SDK
```

---

## 🔑 Key Concepts Learned

### The 3 API Patterns

| API | Library | Returns | How to get a dict |
|-----|---------|---------|-------------------|
| **Jira** | `requests` | Response **object** | `response.json()` |
| **AWS** | `boto3` | **dict** directly | Already a dict ✅ |
| **Azure** | `azure-mgmt-*` | **Iterator** of objects | Loop + `.as_dict()` |

### Universal API Workflow

```
Step 1: Connect to API   →  get an Object (client)
Step 2: Call a method     →  get data as a dictionary
Step 3: Process the dict  →  loops, filters, extract values
```

Step 2 differs by library, but Step 3 is always the same — you process dictionaries.

---

## 🚀 Setup

### Prerequisites
- Python 3.10+
- Jira Cloud instance + API Token ([get one here](https://id.atlassian.com/manage-profile/security/api-tokens))
- AWS credentials configured (`aws configure`)
- Azure credentials configured (`az login`)

### Installation

```bash
git clone <your-repo-url>
cd devops-python

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

```bash
# Jira — fetch issues
python jira/fetch_jira_issues.py

# AWS — fetch EC2 instances
python aws/fetch_ec2_instances.py

# Azure — fetch Virtual Machines
python azure/fetch_vms.py
```

---

## 📓 Learning Resources

- **LEARNING_JOURNAL.md** — Session notes, concepts learned, issues solved
- **flashcards.md** — 33 flashcards for spaced repetition review

---

## 📝 License

This project is for personal learning and interview preparation.
