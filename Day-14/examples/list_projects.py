# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://veerupakshabandi.atlassian.net/rest/api/3/project"

API_TOKEN="ATATT3xFfGF0ZOTZ3OnPrmx7XQYTlOpsFFMnIsxRQz0yfMMVBBg4lJN9DS_ah2cb2tBIHGccpYP7wXXv5qe6aR11ovIaneimoAZe_euR9KZG3iImbA2BwN329PFmQyA76UBspUHvu7Zrfze-icwp0LXJedf9zADsWKLOQXVJydBgdGgBavn_AyM=8CDF2E8E"

auth = HTTPBasicAuth("veerupaksha.bandi@gmail.com", API_TOKEN)

headers = {
  "Accept": "application/json"
}

response = requests.request(
   "GET",
   url,
   headers=headers,
   auth=auth
)

# To print output in the json format please uncomment the below line

#print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))

# To Print project name.
output = json.loads(response.text)

name = output[0]["name"]

print(name)