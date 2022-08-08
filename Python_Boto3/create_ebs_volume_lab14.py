# How to create AWS EBS Volume

import boto3

ec2_client=boto3.client("ec2")

ec2_client.create_volume(AvailabilityZone='us-east-1c',
      Size=8,
    Encrypted=True,
      VolumeType='gp2',
      TagSpecifications=[
          {
              'ResourceType': 'volume',
              'Tags': [
                  {
                      'Key': 'name',
                      'Value': 'Lab14'
                      },
                  ]
          },
        ],
    )
    
    