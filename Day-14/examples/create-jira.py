# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://veerupakshabandi.atlassian.net/rest/api/3/issue"

API_TOKEN = "ATATT3xFfGF0ZOTZ3OnPrmx7XQYTlOpsFFMnIsxRQz0yfMMVBBg4lJN9DS_ah2cb2tBIHGccpYP7wXXv5qe6aR11ovIaneimoAZe_euR9KZG3iImbA2BwN329PFmQyA76UBspUHvu7Zrfze-icwp0LXJedf9zADsWKLOQXVJydBgdGgBavn_AyM=8CDF2E8E"

auth = HTTPBasicAuth("veerupaksha.bandi@gmail.com", API_TOKEN)

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
      "id": "10001"
    },
    "project": {
      "key": "SCRUM"
    },
    "summary": "First JIRA Ticket",
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