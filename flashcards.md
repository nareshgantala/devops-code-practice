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

---

### Card 17

**FRONT:** What is a Python object?

**BACK:** Data + actions bundled together.
```
response.status_code    → data (no parentheses)
response.json()         → action (has parentheses)
```
Strings, lists, API responses, boto3 instances — all objects.
Everything in Python is an object.

---

### Card 18

**FRONT:** `response` vs `response.text` vs `response.json()`?

**BACK:**
`response` → the whole object (box)
`response.text` → body as a string
`response.json()` → body as a Python dict
`response.status_code` → 200, 404, etc.
`response.ok` → True if status is 2xx

---

### Card 19

**FRONT:** Why does `print(response)` show `<Response [200]>` but debugger shows everything?

**BACK:** `print()` shows the object's label only.
The **debugger** expands the object and shows ALL fields.
Use the debugger or access specific fields:
`print(response.text)`
`print(response.status_code)`

---

### Card 20

**FRONT:** Is `response.text` specific to Jira?

**BACK:** No! It comes from the `requests` library.
ANY API call with `requests.get()` gives you:
`.text`, `.json()`, `.status_code`, `.ok`
Works for Jira, GitHub, Azure, Slack — any REST API.

---

### Card 21

**FRONT:** `response.text` vs `response.json()` — what's the difference?

**BACK:**
`.text` → raw string: `'{"issues":[{"id":"10077"}]}'`
`.json()` → parsed dict: `{'issues': [{'id': '10077'}]}`
`.json()` is same as doing `json.loads(response.text)`
Use `.json()` when you need to access keys.

---

### Card 22

**FRONT:** Does AWS boto3 also use `response.json()`?

**BACK:** No! boto3 returns dicts directly — no `.json()` needed.
```
result = ec2.describe_instances()
result["Reservations"]    # already a dict
```
`requests` library → need `.json()` to get dict
`boto3` library → gives you dict directly

---

### Card 23

**FRONT:** `dict["key"]` uses brackets. `object.field` uses dot. When to use which?

**BACK:**
`data["issues"]` → brackets → for dicts you created or parsed from JSON
`response.status_code` → dot → for objects a library gave you
Quick test: did you make it with `{}`? → brackets. Did a library return it? → dot.

---

## Session 2 — 2026-08-22 (AWS & Azure APIs)

---

### Card 24

**FRONT:** What does `boto3.client('ec2')` return?

**BACK:** An **object** (type: `botocore.client.EC2`).
You call methods on it to interact with AWS:
```
client = boto3.client('ec2')
result = client.describe_instances()
```
`client` = object, `result` = dictionary (directly).

---

### Card 25

**FRONT:** What type does `client.describe_instances()` return in AWS boto3?

**BACK:** A **dictionary** — directly! No `.json()` needed.
```
result = client.describe_instances()
type(result)  # <class 'dict'>
result["Reservations"]  # access keys immediately
```

---

### Card 26

**FRONT:** The 3 API patterns — Jira vs AWS vs Azure. How does each return data?

**BACK:**
| API | Returns | To get dict |
|---|---|---|
| Jira (`requests`) | Response **object** | `.json()` |
| AWS (`boto3`) | **dict** directly | Already a dict ✅ |
| Azure SDK | **Iterator** of objects | Loop + `.as_dict()` |

---

### Card 27

**FRONT:** What is the universal pattern for working with any API in Python?

**BACK:**
```
Step 1: Connect → get an Object (client)
Step 2: Call a method → get data as dict
Step 3: Process the dictionary → loops, filters
```
Step 2 differs by library, but Step 3 is always the same.

---

### Card 28

**FRONT:** What is `ItemPaged` in Azure SDK?

**BACK:** An **iterator** — a container that holds objects one by one.
`client.virtual_machines.list_all()` → returns `ItemPaged`
You **cannot** call `.as_dict()` on `ItemPaged` itself.
You must **loop** to get each object out first.

---

### Card 29

**FRONT:** How to convert Azure VM objects to dictionaries?

**BACK:**
```
vms = client.virtual_machines.list_all()

for vm in vms:           # loop through iterator
    vm_dict = vm.as_dict()  # convert EACH object
    print(vm_dict)
```
`.as_dict()` works on each **individual object**, not the iterator.

---

### Card 30

**FRONT:** Azure SDK — `list_*()` vs `get_*()`. What's the difference?

**BACK:**
`list_*()` → returns `ItemPaged` iterator → **loop** + `.as_dict()`
`get_*()` → returns **one** model object → `.as_dict()` directly
```
# list (many) — must loop
for vm in client.virtual_machines.list_all():
    print(vm.as_dict())

# get (one) — no loop
vm = client.virtual_machines.get("rg", "vm-name")
print(vm.as_dict())
```

---

### Card 31

**FRONT:** Why can't we process objects directly? Why do we need dictionaries?

**BACK:** Because dictionaries let us:
- Access data by **key** → `data["name"]`
- **Loop** through items → `for item in data["list"]:`
- **Filter** and **extract** values
Objects hide their data inside methods and attributes.
Our goal: **Object → Dictionary → Process**.

---

### Card 32

**FRONT:** Why don't you name a variable `dict`?

**BACK:** `dict` is a built-in Python type.
If you write `dict = something`, you **shadow** the built-in.
Then `dict()` stops working in your code.
Use descriptive names instead: `vm_dict`, `vm_data`, `response_data`.

---

### Card 33

**FRONT:** Is `.as_dict()` the same as `.json()`?

**BACK:** No! They are from different libraries:
- `.json()` → `requests` library → parses HTTP response body (JSON string → dict)
- `.as_dict()` → Azure SDK → converts Azure model object → dict
Same goal (get a dictionary), different libraries, different method names.
