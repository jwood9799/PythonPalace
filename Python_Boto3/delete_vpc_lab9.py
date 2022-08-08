# How to delete a VPC

import boto3

client=boto3.client("ec2")

response = client.delete_vpc(
    VpcId="vpc-060ea4eff1f33c90b")
    
    