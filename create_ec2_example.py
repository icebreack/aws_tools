#!/usr/bin/env python
import boto3
ec2 = boto3.resource('ec2')
instance = ec2.create_instances(
    ImageId='ami-1e299d7e', #here you change for the image that you'll use... it is easy
    MinCount=1,
    MaxCount=1,
    InstanceType='t2.micro') #here you change the instance type.... caution!
print instance[0].id
