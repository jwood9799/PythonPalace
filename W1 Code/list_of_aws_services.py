# Week 12 Python Project. Create a list of AWS services. Print it and it's length. Remove two items and do the same.

# Create an empty list

aws_services = []

# Append or Input items to your list

aws_services.insert(0, "S3")
aws_services.append('Lambda')
aws_services.append('DynamoDB')
aws_services.append('Cloud9')
aws_services.append('EC2')

# It would be faster to just use the plus/equals operation 

#aws_services += ['S3', 'Lambda', 'DynamoDB', 'Cloud9', 'EC2']

print("Here's my short list of AWS services!")
print(aws_services)
print("It's not a very long list, only", len(aws_services), "items so far.")
print("I plan to continue building onto it later, maybe.")
print("For now I've been instructed to delete a couple of things. I'll start with S3 and DB.")
del aws_services[0]
del aws_services[3]
print("Here's the new shorter list:")
print(aws_services)
print("As you can see it's only", len(aws_services), "items now.")
