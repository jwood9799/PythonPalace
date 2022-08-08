# How to create multiple ec2 instances

import boto3

ec2_resource=boto3.resource("ec2")

ec2_resource.create_instances(ImageId='ami-090fa75af13c156b4',
    InstanceType='t2.micro',
  MaxCount=3,
    MinCount=3)
    
    