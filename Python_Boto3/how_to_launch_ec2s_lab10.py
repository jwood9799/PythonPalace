# How to launch EC2's 

import boto3

ec2_resource=boto3.resource("ec2")

ec2_resource.create_instances(ImageId='ami-090fa75af13c156b4',
    InstanceType='t2.micro',
  MaxCount=1,
    MinCount=1)
    
    