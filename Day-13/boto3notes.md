## What is boto4?
Ans: boto3 is python package which is used interact with aws
1. aws automation with boto3
2. managing ec2 instances, s3 buckets and more


## how boto3 is differ from aws cli, CFT, Terraform?

# Here we can devide them into 2 catagories

    # category 1 is CFT and Terraform
        # These are templating languages, we do not need any programming language skills
        # There can be used when we want use teplating

    # catagory 2 is aws cli and boto3
        # these are scripting language
        # for AWS we can when you want to use scripting.

## Why should i use the scripting?
# if you want to list the resources quickly        

## Why should i use boto3 over awc cli?
# boto3 can be used in serverless programming/functions as well. 
# aws cli will be used in scripting most of the time.


## if you want use boto3 then before that you should install aws cli first.

# $ pip install boto3

# import boto3 module is important
# boto3.client and boto3.resource these both can be used to follow by the resource name.resource will be obsolute in future days.
# boto3 supports botocore


# lambda usage will be decided by architect or developer but not the DevOps engr.

# 1 of the lambda usage is cost optimization and govern the resource usage. For this devops engr has to write the python script.

# This script will run periodically by devops engr automatically through cloud watch because lambda function is event driven, it cannot be run by manually

# everyday devops engr will configure the cron job in cloud watch and as per the schedule job will execute and drive the lambda function.

#



# 