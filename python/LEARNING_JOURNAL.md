# 📓 Learning Journal — Python for Jira Admin & DevOps

## Student Profile
- **Name**: Naresh Gantala
- **Goal**: Senior Jira Admin + Senior DevOps Engineer roles
- **Python Level**: Beginner → learning by doing real Jira/DevOps automation
- **Learning Style**: Mentor mode — I write my own code, AI reviews and explains
- **Jira Instance**: https://nareshjira.atlassian.net (project key: KAN)
- **Python Version**: Python 3.14 (`c:\Users\DELL\AppData\Local\Programs\Python\Python314\python.exe`)

---

## Session 1 — 2026-08-21

### What We Set Up
- [x] Project structure with 4 phases
- [x] `fetch_jira_issues.py` — first working Jira API script
- [x] VS Code debugger (`launch.json` with Python path + cwd)
- [x] Installed `requests` and `python-dotenv` into Python 3.14
- [x] Phase 1 lab templates (1.1, 1.2, 1.3) with tasks + hints
- [x] Mock data files (`mock_jira_response.json`, `bulk_issues.csv`)
- [x] 23 flashcards for spaced repetition

### Concepts Learned
1. **String concatenation** — `domain + "/rest/api/3/search"` and f-strings
2. **dotenv** — `load_dotenv()` + `os.getenv()` to load secrets
3. **pip install pitfall** — `python -m pip` vs bare `pip` (multiple Python versions)
4. **JSON basics** — what JSON is, `json.load` vs `loads` vs `dump` vs `dumps`
5. **Python objects** — data + actions, dot notation, `response.text` vs `response.json()`
6. **Dict vs Object** — brackets `["key"]` for dicts, dot `.field` for objects
7. **Debugger** — Watch panel shows all fields, Debug Console lets you call methods
8. **response.text vs response.json()** — string vs parsed dict
9. **requests library** — `.text`, `.json()`, `.status_code` work for ANY API, not just Jira
10. **boto3 difference** — returns dicts directly, no `.json()` needed

### Issues Solved
- `ModuleNotFoundError: No module named 'requests'` — installed into wrong Python
- `MissingSchema` error — was using literal string "JIRA_DOMAIN" instead of `os.getenv()`
- `TypeError: Object of type Response is not JSON serializable` — used `response.json()` instead
- Debugger not working — added `python` path and `cwd` to `launch.json`

### Where I Stopped
- **Lab 1.1**: NOT STARTED — ready to begin Task 1 (load JSON, print metadata)
- **Lab 1.2**: NOT STARTED
- **Lab 1.3**: NOT STARTED
- `fetch_jira_issues.py` is working and connects to real Jira

### Key Files
- `flashcards.md` — 23 cards for spaced repetition review
- `jira/phase1_fundamentals/lab1_1_nested_dict_parsing.py` — Start here next
- `jira/phase1_fundamentals/data/mock_jira_response.json` — Study this data first

---

## Next Session — TODO
- [ ] Start Lab 1.1 Task 1: Load JSON and print top-level metadata
- [ ] Complete Lab 1.1 Tasks 2-8
- [ ] Start Lab 1.2: CSV/JSON ETL
- [ ] Review flashcards (spaced repetition)
