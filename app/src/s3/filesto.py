import os
import boto3

from datetime import datetime

s3_user = os.environ.get("S3_USER")
s3_password = os.environ.get("S3_PASSWORD")
s3_host = os.environ.get("S3_HOST")
s3_port = os.environ.get("S3_PORT")
# TODO: Need to find a more dynamic way to retrieve the bucket
s3_bucket = os.environ.get("S3_BUCKET")


s3_config = {
    "service_name": "s3",
    "aws_access_key_id": s3_user,
    "aws_secret_access_key": s3_password,
    "endpoint_url": f"http://{s3_host}:{s3_port}",
    "verify": False
}

s3 = boto3.resource(**s3_config)


def upload_file(file: any) -> str:
    """
    Upload a file to minio storage.

    :param the file that needs to be uploaded
    :return the url that the file can be located at
    """

    try:
        bucket = s3_bucket
        timestamp = datetime.utcnow().isoformat()
        filetype = file.filename.split('.')[-1]
        filename = f"{timestamp}{filetype}"

        s3.Bucket(bucket).Object(filename).put(Body=file.read())

        return get_public_s3_url(filename)
    except Exception as e:
        return {"error": str(e)}


def get_public_s3_url(filename: str) -> str:
    return f"http://{s3_host}:{s3_port}/card-images/{filename}"
