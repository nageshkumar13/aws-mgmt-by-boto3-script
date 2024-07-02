import boto3

AWS_REGION = ["ap-south-1"]
for region in AWS_REGION:
    client = boto3.client('ecr', region_name=region)
    imageTags = []
    def latest_two_images(repoName, imageTags):
        response = client.describe_images(repositoryName=repoName)
        images = response['imageDetails']
        # Sort the list of images by creation date
        sorted_images = sorted(images, key=lambda x: x['imagePushedAt'], reverse=True)
        # Get the last 2 images
        latest_images = sorted_images[:2]
        # Print the image digests
        for img in latest_images:
            imageTags.append(img['imageTags'][0])
        return imageTags