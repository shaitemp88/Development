# Modules import
import os
import boto3

# import uuid

# Project configuration settings - Environment variables
AWS_ID = os.environ['aws_access_key_id']
AWS_KEY = os.environ['aws_secret_access_key']
REGION = os.environ['region']
INTERVAL = os.environ["INTERVAL"]

print("=                   =")
print("Envoronment Variable:")
print(AWS_ID)
print(AWS_KEY)
print(REGION)
print(INTERVAL)
print("=====================")


ec2 = boto3.resource('ec2', region_name=REGION)
instances = ec2.instances.filter(Filters=[{'Name': 'tag:k8s.io/role/master', 'Values': ["1"]}, {'Name': 'instance-state-code', 'Values': ["16"]}])
for instance in instances:
    for tag in instance.tags:
        print(tag)
    print("instance id: ", instance.id)


print("===============!!!FIINSHED!!!===============")
