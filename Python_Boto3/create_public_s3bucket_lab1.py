# How to create a public S3 bucket

import boto3

aws_resource=boto3.resource("s3")

bucket=aws_resource.Bucket("pythonboto3lab1")

response = bucket.create(
    ACL='public-read',
    CreateBucketConfiguration={
        'LocationConstraint': 'us-east-2'
    },
  
)

print(response)