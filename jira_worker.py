# Imports
import requests
from requests.auth import HTTPBasicAuth
import json

# CONSTANTS
JIRA_DOMAIN = "rahulmandarapu.atlassian.net"
EMAIL = "rahul.mandarapu1@gmail.com"
API_TOKEN = "ATATT3xFfGF0qm1FX3XbeIY7GfsfHVe5U0qAOJBdptqqgvx-FjkDuLskScM72kweI_akayKC-wTvNnSS-oYlGnpqIUGGUL5jts2CmdYmdAsKveGs4yy1rNamKv6UkKQTsHnlDVgm0w4UkDKbhj9LxDM8GC8UqXL49tewakweU34K8irAWyMd8g4=5C7C0F7D"

PROJECT_KEY = "SCRUM"
ISSUE_TYPE = "Task"
SUMMARY = "Example issue created via API"
DESCRIPTION = "This issue was created by a Python script."

# ISSUE GEN
url = f"https://{JIRA_DOMAIN}/rest/api/3/issue"

auth = HTTPBasicAuth(EMAIL,API_TOKEN)

headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
}

payload = {
        "fields": {
        "project": {
            "key": PROJECT_KEY
        },
        "summary": SUMMARY,
        "description": {
            "type": "doc",
            "version": 1,
            "content": [
                {
                    "type": "paragraph",
                    "content": [
                        {
                            "type": "text",
                            "text": DESCRIPTION
                        }
                    ]
                }
            ]
        },
        "issuetype": {
            "name": ISSUE_TYPE
        }
    }
}

response = requests.post(
    url,
    headers=headers,
    auth=auth,
    data=json.dumps(payload)
)

if response.status_code == 201:
    issue_key = response.json()["key"]
    print(f"Issue created successfully: {issue_key}")
else:
    print("Failed to create issue")
    print(response.status_code)
    print(response.text)

## Adding comment for practice
print("Is this appearing on Jira")

