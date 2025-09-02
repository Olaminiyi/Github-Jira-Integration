from flask import Flask, jsonify, request
import requests
from requests.auth import HTTPBasicAuth
import json
from dotenv import load_dotenv
import os

app = Flask(__name__)

# Load env once
load_dotenv()
api_token = os.getenv("JIRA_TOKEN")
email = os.getenv("EMAIL")

@app.route('/createJira', methods=['POST'])
def createJira():
    # get webhook payload from GitHub
    data = request.get_json()

    comment_body = data.get("comment", {}).get("body", "")
    issue_topic = data.get("issue", {}).get("title", "")

    if comment_body.strip() != "/jira":
        return jsonify({"message": "To create ticket your comment must be: /jira"}), 200

    # Jira setup
    url = "https://olaiya-olaminiyi.atlassian.net/rest/api/3/issue"
    auth = HTTPBasicAuth(email, api_token)

    headers = {
      "Accept": "application/json",
      "Content-Type": "application/json"
    }

    payload = {
        "fields": {
            "description": {
                "content": [
                    {
                        "content": [
                            {
                                "text": "My first Jira ticket.",
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
            "summary": issue_topic,
        }
    }

    response = requests.post(
       url,
       json=payload,
       headers=headers,
       auth=auth
    )

    return jsonify(response.json()), response.status_code

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
