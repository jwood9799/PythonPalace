# How to create a private S3 bucket

import boto3

aws_resource=boto3.resource("s3")

bucket=aws_resource.Bucket("pythonboto3lab1.2")

response = bucket.create(
    ACL='private', 
    CreateBucketConfiguration={
        'LocationConstraint': 'us-east-2'
    },
  
)

print(response)