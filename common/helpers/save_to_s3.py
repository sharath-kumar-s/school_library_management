import base64
import io
import boto3
import logging
from botocore.config import Config
from django.conf import settings
from botocore.exceptions import ClientError

s3 = boto3.resource(
    's3',
    aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
    aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
    region_name=settings.AWS_S3_REGION_NAME,
    config=Config(signature_version=settings.AWS_S3_SIGNATURE_VERSION)
)

s3_client = boto3.client(
    's3',
    aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
    aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
    region_name=settings.AWS_S3_REGION_NAME,
    config=Config(signature_version=settings.AWS_S3_SIGNATURE_VERSION)
)


def create_presigned_url(bucket_name, object_name, expiration=int(settings.PRE_SIGNED_URL_EXPIRATION_TIME_IN_SEC)):
    try:
        pre_signed_url = s3_client.generate_presigned_url('get_object',
                                                          Params={'Bucket': bucket_name,
                                                                  'Key': object_name},
                                                          ExpiresIn=expiration)
    except ClientError as e:
        logging.error(e)
        return None, None
    return pre_signed_url


def save_base64_to_s3(s3_bucket_name, file_name_with_folder, base64_str):
    try:
        obj = s3.Object(s3_bucket_name, file_name_with_folder)
        obj.put(Body=base64.b64decode(base64_str), ACL='public-read')
    except Exception as e:
        logging.error(e)


def save_base64_to_public_s3(s3_bucket_name, file_name_with_folder, base64_str):
    save_base64_to_s3(s3_bucket_name, file_name_with_folder, base64_str)
    return create_presigned_url(s3_bucket_name, file_name_with_folder)


def save_base64_to_public_s3_get_url(s3_bucket_name, file_name_with_folder, base64_str):
    save_base64_to_s3(s3_bucket_name, file_name_with_folder, base64_str)
    location = s3_client.get_bucket_location(Bucket=s3_bucket_name)['LocationConstraint']
    object_url = "https://%s.s3-%s.amazonaws.com/%s" % (
        s3_bucket_name, location, file_name_with_folder)
    return object_url


def save_pdf_to_public_s3_get_url(s3_bucket_name, file_name_with_folder, file_content):
    s3_client.upload_fileobj(io.BytesIO(file_content), s3_bucket_name, file_name_with_folder, ACL='public-read')
    location = s3_client.get_bucket_location(Bucket=s3_bucket_name)['LocationConstraint']
    object_url = "https://%s.s3-%s.amazonaws.com/%s" % (
        s3_bucket_name, location, file_name_with_folder)
    return object_url


def delete_s3_object(s3_bucket_name, file_name_with_folder):
    try:
        s3_client.delete_object(
            Bucket=s3_bucket_name,
            Key=file_name_with_folder
        )
    except Exception as e:
        logging.error(str(e))
        pass


def get_files_in_bucket(s3_bucket_name, prefix_str):
    details_list = []
    objs = s3.Bucket(s3_bucket_name).objects.filter(
        Prefix=prefix_str)
    location = s3_client.get_bucket_location(Bucket=s3_bucket_name)['LocationConstraint']
    for obj in objs:
        report_name = obj.key[obj.key.rfind("/") + 1:-4]
        if report_name:
            details_list.append({
                "name": report_name,
                "url": "https://%s.s3-%s.amazonaws.com/%s" % (s3_bucket_name, location, obj.key)
            })
    return details_list


def get_details_of_files_in_bucket(report_type, date, s3_bucket_name, prefix_str):
    details_list = []
    objs = s3.Bucket(s3_bucket_name).objects.filter(
        Prefix=prefix_str)
    for obj in objs:
        object_url = create_presigned_url(s3_bucket_name, obj.key)
        report_name = obj.key[obj.key.rfind("/") + 1:-4]
        details_list.append({
            "type": report_type,
            "name": report_name,
            "date": date,
            "url": object_url
        })
    return details_list


def get_details_of_file_in_bucket(report_type, date, s3_bucket_name, prefix_str):
    report_name = ""
    object_url = ""
    objs = s3.Bucket(s3_bucket_name).objects.filter(
        Prefix=prefix_str)
    for obj in objs:
        object_url = create_presigned_url(s3_bucket_name, obj.key)
        report_name = obj.key[obj.key.rfind("/") + 1:-4]
        break
    return {
        "type": report_type,
        "name": report_name,
        "date": date,
        "url": object_url
    }


def get_file_link_from_s3(s3_bucket_name, file_name):
    object_url = ''
    objs = s3.Bucket(s3_bucket_name).objects.filter(
        Prefix=file_name)
    if list(objs.limit(1)):
        get_latest_obj = lambda obj: obj.key[obj.key.rfind("/") + 1:-4]
        key = (sorted(objs, key=get_latest_obj, reverse=True)[0]).key
        object_url = create_presigned_url(s3_bucket_name, key)
    return object_url


def get_last_modified_time_of_file(s3_bucket_name, file_name):
    response = s3_client.list_objects_v2(Bucket=s3_bucket_name, Prefix=file_name)
    all = response['Contents']
    if len(all) > 0:
        latest = max(all, key=lambda x: x['LastModified'])
        return latest['LastModified']
    else:
        return None


def get_object_from_s3(s3_bucket_name, file_name):
    objs = s3.Bucket(s3_bucket_name).objects.filter(
        Prefix=file_name)
    if list(objs.limit(1)):
        get_latest_obj = lambda obj: obj.key[obj.key.rfind("/") + 1:-5]
        return sorted(objs, key=get_latest_obj, reverse=True)[0]
    return None
