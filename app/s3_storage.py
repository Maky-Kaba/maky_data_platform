import boto3

def upload_to_s3(local_file_path, bucket_name, s3_object_name):
    """
    Uploads a local file to an S3 bucket.

    :param local_file_path: Path to the file to upload.
    :param bucket_name: The name of the target S3 bucket.
    :param s3_object_name: The desired name of the object in S3.
    """
    # Create an S3 client. Boto3 will automatically find your
    # configured credentials from 'aws configure'.
    s3_client = boto3.client('s3')

    try:
        # 'with open' ensures the file is closed properly
        with open(local_file_path, 'rb') as f:
            s3_client.upload_fileobj(f, bucket_name, s3_object_name)
        
        print(f"Successfully uploaded '{local_file_path}' to 's3://{bucket_name}/{s3_object_name}'")
        return True
    except FileNotFoundError:
        print(f"Error: The file '{local_file_path}' was not found.")
        return False
    except Exception as e:
        # This will catch other errors, like if the bucket doesn't exist
        # or you don't have permissions.
        print(f"An error occurred: {e}")
        return False