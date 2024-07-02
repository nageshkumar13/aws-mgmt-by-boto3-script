import boto3

AWS_REGION = ["ap-south-1"]
for region in AWS_REGION:
    client = boto3.client("ec2",region_name=region)
    instance_ids=[]
    def get_ec2_details():
        reservations = client.describe_instances()
        for reservation in reservations['Reservations']:
            for instance in reservation['Instances']:
                if instance['State']['Name'] == 'stopped':
                   instance_ids.append(instance['InstanceId'])
        
        print(instance_ids)
        return instance_ids
    def start_ec2_instances(instance_ids):
        for ec2_id in instance_ids:
            response = client.start_instances(InstanceIds=[ec2_id])
            print(f"{response['StartingInstances'][0]['InstanceId']} was {response['StartingInstances'][0]['PreviousState']['Name']}, but now is {response['StartingInstances'][0]['CurrentState']['Name']}.")
    instance_ids = get_ec2_details()
    start_ec2_instances(instance_ids)


     