# install boto3 : pip install boto3
# refer the boto3 document to create s3 bucket
# open docs, available service/s3/create bucket and here you just mention required thing.

import boto3

client = boto3.client('s3')

#Create bucket from python using boto3

#response = client.create_bucket(
#    Bucket='bucket-boto3-viru3',
#)
#print(response)

# python test.py

# Get bucket acl from from the bucket that has been created above.

response = client.get_bucket_acl(
    Bucket='bucket-boto3-viru3',
)

print(response)
