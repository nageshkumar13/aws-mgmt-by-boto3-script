import boto3
import datetime
import re
import botocore

def get_snapshot_details(pattern, client):
        snapshots = client.describe_snapshots(OwnerIds=['_________'])
        print(snapshots)
        print(len(snapshots['Snapshots']))
        for snapshot in snapshots['Snapshots']:
            description = snapshot['Description']
            print(description)
            match = re.search(pattern,description)
            if match:
                startTimeobj = snapshot['StartTime']
                startTime = startTimeobj.date()
                currentTime = datetime.datetime.now().date()
                diffTime = currentTime - startTime
                #print(f"{diffTime}")
                if (diffTime.days > 10 and snapshot['State'] == 'completed'):
                    snapshot_ids.append(snapshot['SnapshotId'])
        print('Snapshot IDs are :',snapshot_ids)  
        print('Region for Snapshots is :',region)
        return snapshot_ids
def delete_snapshots_daily(snapshot_ids):
    for snapshot_id in snapshot_ids:
        try:
            response = client.delete_snapshot(SnapshotId=snapshot_id)  
            print("Snapshot with ID {} has been deleted.".format(snapshot_id))
        except botocore.exceptions.ClientError as e:
            if e.response['Error']['Code'] == 'InvalidSnapshot.NotFound':
                print("Snapshot with ID {} does not exist.".format(snapshot_id)) 
            else:
                raise e


AWS_REGION = ["ap-south-1"]
for region in AWS_REGION:
    
    client = boto3.client("ec2",region_name=region)
    snapshot_ids=[]
    pattern = "Demo.*"
    snapshot_ids = get_snapshot_details(pattern, client)
    delete_snapshots_daily(snapshot_ids)

    