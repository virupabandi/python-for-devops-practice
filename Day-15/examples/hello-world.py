#flask installation in ubuntu

# sudo apt update
#sudo apt install python3-pip python3-setuptools
#sudo apt install python3-venv
#python3 -m venv myflaskenv
#source myflaskenv/bin/activate
#pip3 install Flask
#pip3 show flask

# flask comes with an inbuilt server
# Importing a Flask module from flask package
#from flask import Flask

# Create a flask application instance
#app = Flask(__name__)

# defination funtion, before execution of any function we should use the decorator. 
# what is decorator, decorator is used to call the perticular action befor the function.
# Decorator starts with @

#@app.route('/')
#def hello_world():
#    return 'Hello, World!'

#if __name__ == '__main__':
#    app.run("0.0.0.0")



from flask import Flask

app = Flask(__name__)

#@app.route("/")
#def hello():
@app.route("/createJIRA". methods=[POST])
def createJIRA():
    import requests
    from requests.auth import HTTPBasicAuth
    import json

    url = "https://url.atlassian.net/rest/api/3/issue"

    auth = HTTPBasicAuth("example@example.com", "api_token")

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

    return(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))
  

app.run('0.0.0.0', port=5000)