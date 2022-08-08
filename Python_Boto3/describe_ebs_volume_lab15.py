# How to describe AWS EBS Volume

import boto3

ec2=boto3.client("ec2")

response=ec2.describe_volumes()

data=response["Volumes"]

with io.open("volume.csv","w",encoding="utf-8")as f1:
    f1.write("device,volumeid,instanceid,size\n")
    for volume in data:
        
     volume_data=volume["Attachments"]
     if(len(volume_data)>0):
         device=volume["Attachments"][0]["Device"]
         instance_id=volume["Attachments"][0]["InstanceId"]
         
     else:
        device="not attached"
        instance_id="not attached"
     volume_id=volume["VolumeId"]
     size=volume["Size"]
     f1.write(device+","+volume_id+","+instance_id+","+str(size)+"\n")
         
         