# How to list bucket objects.

import boto3

s3_resource=boto3.client("s3")

objects=s3_resource.list_objects(Bucket="pythonboto3lab1.2") ["Contents"]

len(objects)

if len(objects)>0:
    print("objects exist")
    
for object in objects:
    print(object["Key"])
    
