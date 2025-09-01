import requests
from requests.auth import HTTPBasicAuth
import json
from dotenv import load_dotenv
import os

load_dotenv()
api_token = os.getenv("JIRA_TOKEN")
email = os.getenv("EMAIL")

url = "https://olaiya-olaminiyi.atlassian.net/rest/api/3/project"

auth = HTTPBasicAuth(email, api_token)

headers = {
  "Accept": "application/json"
}

response = requests.request(
   "GET",
   url,
   headers=headers,
   auth=auth
)

#print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))
output = json.loads(response.text)
name = output[0]["name"]
print(name)