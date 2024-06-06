# **# Github-JIRA intergration Project

# **## Github-JIRA integration Project

# Manual process in Jira
# 1. QE team will go to jira portal/backlog/create ticket in the backlog.

## Jira automation process

# Problem statement

# task given to devops engr by developer is they have to integrate jira with github.

# Solution
# 1. host python application in an ec2 instance.


# 2. Configure the ec2 webhook in github
# 3. QE team or dev team if they tested and find there is bug in the code or application or product.
# Then they need not to go to jira portal and create a ticket manually.
# 4. DevOps engineer will automate the hole process by following below steps.
  #  - DevOps engr hosts a python application on an ec2 instances
   # - configure ec2/application webhook on the github and there will be a repository for jira automation. here a url of python application has been configured
   # - whenever QE team finds bug in code, they just have to go to comment /jira or message in the github repository
   # Then after github will collect ticket records in the json format and sends to the python application which is hosted  on EC2.
   # After that the python application  makes API call to the jira dashboard and sends the json format to the jira.
    


