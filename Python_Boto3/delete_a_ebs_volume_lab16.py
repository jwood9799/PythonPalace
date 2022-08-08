# How to delete an EBS Volume

import boto3
ec2_client=boto3.client("ec2")

ec2_client.delete_volume( VolumeId='vol-0f680180a4bedda72')

