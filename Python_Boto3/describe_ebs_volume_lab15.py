# How to describe AWS EBS Volume

import boto3

ec2=boto3.client("ec2")

response=ec2.describe_volumes()

data=response["Volumes"]

for volume in data:
    volume_data=volume["Attachments"]
    
    