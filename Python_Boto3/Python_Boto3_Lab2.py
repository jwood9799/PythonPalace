# How to list your S3 buckets.

import boto3

resource=boto3.resource

resource=boto3.resource("s3")

list(resource.buckets.all())

