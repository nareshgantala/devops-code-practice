import os
import requests
from requests.auth import HTTPBasicAuth
import json
from dotenv import load_dotenv

load_dotenv()

url = os.getenv("JIRA_DOMAIN") + "/rest/api/3/search/jql"

auth = HTTPBasicAuth(os.getenv("JIRA_EMAIL"), os.getenv("API_TOKEN"))

headers = {
  "Accept": "application/json"
}

query = {
  'jql': 'project = KAN'
}

response = requests.request(
   "GET",
   url,
   headers=headers,
   params=query,
   auth=auth
)