# Use boto3 library to interact with AWS services
# Install boto3 using
# >> pip install boto3

import boto3
from botocore.exceptions import NoCredentialsError

def upload_to_aws(file_path, bucket_name, s3_file_name):
    # Provide your AWS credentials
    aws_access_key = 'YOUR_AWS_ACCESS_KEY'
    aws_secret_key = 'YOUR_AWS_SECRET_KEY'

    # Create a new S3 client
    s3 = boto3.client('s3', aws_access_key_id=aws_access_key, aws_secret_access_key=aws_secret_key)

    try:
        # Upload the file to the specified bucket with the given name
        s3.upload_file(file_path, bucket_name, s3_file_name)
        return True
    except NoCredentialsError:
        return False

# Example usage
file_path = 'path/to/your/file.txt'
bucket_name = 'your-bucket-name'
s3_file_name = 'file.txt'
upload_to_aws(file_path, bucket_name, s3_file_name)
# Please Like and Subscribe