# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://veerupakshabandi.atlassian.net/rest/api/3/project"

API_TOKEN=""

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