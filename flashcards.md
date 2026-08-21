# 🃏 Flashcards — Write on Index Cards

---

### Card 1

**FRONT:** Why does `pip install requests` sometimes not work?

**BACK:** `pip` may point to a different Python. Use:
`python -m pip install requests`
This ensures it installs into the Python you're actually using.

---

### Card 2

**FRONT:** How to check which Python you're using?

**BACK:**
`python --version` → shows version
`where.exe python` → shows all paths (Windows)
First path in list = the one that runs.

---

### Card 3

**FRONT:** How to load secrets from a `.env` file?

**BACK:**
```
from dotenv import load_dotenv
import os
load_dotenv()
token = os.getenv("API_TOKEN")
```
Never hardcode secrets. Add `.env` to `.gitignore`.

---

### Card 4

**FRONT:** Two ways to build a URL from a variable?

**BACK:**
```
# Concatenation
url = domain + "/rest/api/3/search"

# f-string (preferred)
url = f"{domain}/rest/api/3/search"
```

---

### Card 5

**FRONT:** `os.getenv("KEY")` vs `os.environ["KEY"]`?

**BACK:**
`os.getenv("KEY")` → returns `None` if missing (safe)
`os.environ["KEY"]` → crashes with `KeyError` if missing
Use `getenv()` unless you want it to crash.

---

### Card 6

**FRONT:** How to safely access a dict key that might be `null`?

**BACK:**
```
# Crashes if missing:
data["assignee"]["name"]

# Safe:
assignee = data.get("assignee")
if assignee is not None:
    name = assignee["name"]
```
Use `.get()` when key might not exist.

---

### Card 7

**FRONT:** `json.load` vs `json.loads` vs `json.dump` vs `json.dumps`?

**BACK:**
`load(file)` → file → dict
`loads(string)` → string → dict
`dump(data, file)` → dict → file
`dumps(data)` → dict → string
The **s** = **s**tring.

---

### Card 8

**FRONT:** What values are "falsy" in Python?

**BACK:**
`None`, `""`, `0`, `[]`, `{}`, `False`
All evaluate to `False` in an `if` statement.
`if not value:` catches all of them.
`if value is None:` checks only for `None`.

---

### Card 9

**FRONT:** Write a list comprehension pattern.

**BACK:**
```
[WHAT for ITEM in LIST if CONDITION]
```
Example — find unassigned issue keys:
```
[i["key"] for i in issues
 if i["fields"]["assignee"] is None]
```

---

### Card 10

**FRONT:** How to get unique values from a list?

**BACK:**
```
projects = ["KAN", "OPS", "KAN"]
unique = set(projects)  # {"KAN", "OPS"}
```
`list` = duplicates OK, ordered
`set` = no duplicates, unordered

---

### Card 11

**FRONT:** What is JSON?

**BACK:** A text format for storing data. Looks like Python dicts.
Used by: Jira API, AWS CLI, Kubernetes, Terraform.
File extension: `.json`
Your `launch.json` and Jira API responses are JSON.

---

### Card 12

**FRONT:** JSON vs Python — what's different?

**BACK:**
```
JSON       →  Python
null       →  None
true       →  True
false      →  False
```
Everything else (strings, numbers, lists, dicts) looks the same.

---

### Card 13

**FRONT:** How to read a JSON file into Python?

**BACK:**
```
import json

with open("data.json", "r") as f:
    data = json.load(f)

print(data["total"])
```
`json.load(f)` converts the file content into a Python dict.

---

### Card 14

**FRONT:** How to access nested JSON?
`{"issues": [{"fields": {"status": {"name": "To Do"}}}]}`

**BACK:** Chain the keys step by step:
```
data["issues"]                         → list
data["issues"][0]                      → first issue
data["issues"][0]["fields"]            → fields dict
data["issues"][0]["fields"]["status"]  → status dict
data["issues"][0]["fields"]["status"]["name"] → "To Do"
```

---

### Card 15

**FRONT:** How to pretty-print a dict to see its structure?

**BACK:**
```
import json
print(json.dumps(data, indent=2))
```
`indent=2` adds spacing so you can read the nested structure.
Use this to debug API responses.

---

### Card 16

**FRONT:** Where will you see JSON in DevOps work?

**BACK:**
- Jira API → sends/receives JSON
- AWS CLI → output is JSON
- `launch.json` → VS Code config
- Terraform state → JSON
- Kubernetes → JSON or YAML
- REST APIs → all use JSON
