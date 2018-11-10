# -*- coding: utf-8 -*- 

# Boto 3
import boto3
import time
import sys
ec2 = boto3.resource('ec2',region_name='us-east-1')

def create_instnaces():
    #create instnaces.
    ec2_instances = ec2.create_instances(ImageId='ami-013be31976ca2c322',MinCount=1,MaxCount=1)
    

    for instance in ec2_instances:
        while instance.state != "running":
            print '...instance is {state}'.format(state=instance.state)
            sys.stdout.flush()
            time.sleep(5)
    
    return ec2_instances


def terminate_instances(instances):
    #terminate instances in ec2_instances arrן
    for instance in ec2.instances.filter(InstanceIds=ec2_instances):
        print instance
        instance.terminate()




