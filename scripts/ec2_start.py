#!/usr/bin/python
'''
This script starts all instances with a specific tag.
'''

import boto3

def instances_find(name, value):
    '''
    Finds instance id's based on tags.
    Returns a list of instances found.
    '''
    list_instances = []
    # filter based on tags
    filters =[
        {
        'Name': name,
        'Values': [
            value,
            ]
        },
    ]
    instances = ec2_resource.instances.filter(Filters=filters)
    for instance in instances:
        # for each instance, append to list
        list_instances.append(instance.id)
    return list_instances

def instances_start(list):
    '''
    Starts instances defined in the list.
    '''
    ec2_client.start_instances(InstanceIds=list)

# enter tag name and value
tag_name = 'tag:environment'
tag_value = 'dev'

ec2_resource = boto3.resource('ec2')
ec2_client = boto3.client('ec2')

# find instances
ec2_list = instances_find(tag_name, tag_value)
# start instances
ec2_stop = instances_start(ec2_list)
print('started instances: ' + str(ec2_list))
