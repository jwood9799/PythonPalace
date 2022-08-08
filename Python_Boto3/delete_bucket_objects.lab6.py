# How to delete objects from s3 buckets.

import boto3

s3_resource=boto3.client("s3")


# Delete a single object
s3_resource.delete_object(Bucket='pythonboto3lab1.2',
    Key='uploadtest.png')

# Delete multiple objects
import os
import glob

#find all the objects in your buckets
objects=s3_resource.list_objects(Bucket="pythonboto3lab1.2")["Contents"]

# Iteration
for object in objects:
    s3_resource.delete_object(Bucket="pythonboto3lab1.2",
      Key=object["Key"])
      
      
     