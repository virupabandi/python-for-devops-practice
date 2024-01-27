# Tasks

# Get pull request information on a github repository using python?
        # Here our task is python has to talk to github api.
        # python will talk to github api through a its own module called REQUEST module.


# Steps for the task.
    # step1: Install and import REQUEST module (pip install requests)
    # step2: configure the github api url in order to python talk to github for pull request.
            # to get github api url: github api docs/rest api/pulls/pulls/

    # step3: Once you receive the information form github, you have to convert the json format in to dictionary. because 
            # received information is in the json format and python cannot read json.
    # step4: print the required thing

# pip install requests 

# if does not work run below command and pip install requests

# apt install imagemagick-6.q16hdri -y



import requests

response = requests.get("https://api.github.com/repos/kubernetes/kubernetes/pulls")   #response is variable here and it is an object
# variable or object = module.get("github api url")

print(response)  #print the file now python filename.py

print(type(response))     #print the file now python filename.py

#print(response.json())    #print the file now python filename.py, we get complete output of the url.

print(response.status_code)     #print the file now python filename.py. you get status code

complete_detail = response.json()    # python filename.py
print(complete_detail[0]["id"])      # python filename.py. printing id of the zero number using list

print(complete_detail[0]["user"]["login"])

# now we have to print all user login name in the above url using for loop

for i in range(len(complete_detail)):
    print(complete_detail[i]["user"]["login"])