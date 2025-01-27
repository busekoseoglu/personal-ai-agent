import boto3
from botocore.exceptions import NoCredentialsError

# Function to upload file to S3
def upload_to_s3(file, bucket="*****", object_name=None):
    """
    Uploads a file-like object to an S3 bucket.
    
    :param file: File-like object from Streamlit file uploader
    :param bucket: Name of the S3 bucket
    :param object_name: S3 object name (default is the file name)
    :return: Public URL of the uploaded file if successful, else None
    """
    # Initialize S3 client
    s3 = boto3.client('s3')

    # Use the uploaded file's name as the S3 object name if not provided
    if object_name is None:
        object_name = file.name

    try:
        # Upload the file to S3
        s3.upload_fileobj(file, bucket, object_name, ExtraArgs={"ACL": "public-read"})

        # Construct the file's public URL
        region = s3.get_bucket_location(Bucket=bucket)["LocationConstraint"]
        file_url = f"https://{bucket}.s3.{region}.amazonaws.com/{object_name}"
        return file_url
    except FileNotFoundError:
        print(f"The file '{file.name}' was not found.")
    except NoCredentialsError:
        print("Credentials not available.")
    except Exception as e:
        print(f"An error occurred: {e}")

    return None
