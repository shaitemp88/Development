# Modules import
import os
import boto3

# import uuid

# Project configuration settings - Environment variables
AWS_ID = os.environ['aws_access_key_id']
AWS_KEY = os.environ['aws_secret_access_key']
REGION = os.environ['region']
INTER  = os.environ['interval']
# AWS_ID = os.environ.get('aws_access_key_id')
# AWS_KEY = os.environ.get('aws_secret_access_key')
# REGION = os.environ.get('region')


print("=                   =")
print("Envoronment Variable:")
print(AWS_ID)
print(AWS_KEY)
print(REGION)
print(INTER)
print("=====================")


ec2_resource = boto3.resource('ec2', region_name=REGION)
instances = ec2_resource.instances.filter(
    Filters=[{'Name': 'tag:k8s.io/role/master', 'Values': [1]}, {'Name': 'instance-state-code', 'Values': [16]}])
for instance in instances:
    print(instance.id, instance.instance_type)


print("===============!!!FIINSHED!!!===============")
