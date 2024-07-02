import boto3

def get_volume_details(client):
    volumes = client.describe_volumes()
    for volume in volumes['Volumes']:
        if volume['State'] == 'available':
            volume_ids.append(volume['VolumeId'])
    print(volume_ids)
    return volume_ids
def terminate_volumes(volume_ids):
    for vol in volume_ids:
        response = client.delete_volume(VolumeId=vol)
        print(response)



AWS_REGION = ["ap-south-1"]
for region in AWS_REGION:
    client = boto3.client("ec2",region_name=region)
    volume_ids=[]       
    volume_ids = get_volume_details(client)
    terminate_volumes(volume_ids)