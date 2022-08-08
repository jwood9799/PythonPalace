# How to upload a file to an S3 bucket. The file must be in your home location. Or at least that's the only way I could get it to work.  

import boto3

s3_resource=boto3.client("s3")

s3_resource.upload_file(
    Filename="testfile",
    Bucket="pythonboto3lab1.2",
    Key="uploadtest1.png")

