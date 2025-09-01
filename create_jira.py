import requests
from requests.auth import HTTPBasicAuth
import json
from dotenv import load_dotenv
import os

load_dotenv()
api_token = os.getenv("JIRA_TOKEN")
email = os.getenv("EMAIL")

url = "https://olaiya-olaminiyi.atlassian.net/rest/api/3/issue"

auth = HTTPBasicAuth(email, api_token)

headers = {
  "Accept": "application/json",
  "Content-Type": "application/json"
}

payload = json.dumps( {
  "fields": {
   
    "description": {
      "content": [
        {
          "content": [
            {
              "text": "My first Jira tickect.",
              "type": "text"
            }
          ],
          "type": "paragraph"
        }
      ],
      "type": "doc",
      "version": 1
    },
 
    "issuetype": {
      "id": "10003"
    },
   
    "project": {
      "key": "ECP"
    },
   
    "summary": "First Jira Ticket",
    
   
  },
  "update": {}
} )

response = requests.request(
   "POST",
   url,
   data=payload,
   headers=headers,
   auth=auth
)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))

