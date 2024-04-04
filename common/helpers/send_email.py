from django.contrib.auth.models import User
import boto3
from botocore.exceptions import ClientError

from common.helpers.validators.string_validators import is_valid_email_id
from school_management import settings


def check_if_user_is_dnd(user_email_notification):
    if user_email_notification is True:
        return True
    return False


def send_email(subject, body, to_email):
    client = boto3.client('ses', region_name=settings.AWS_REGION)
    mail_list = []
    if isinstance(to_email, list):
        for email in to_email:
            if is_valid_email_id(email):
                mail_list.append(email)
    else:
        if not is_valid_email_id(to_email):
            return
        if User.objects.filter(email=to_email) and check_if_user_is_dnd(User.objects.filter(email=to_email).first()):
            return
        mail_list = to_email
    try:
        response = client.send_email(
            Destination={
                'ToAddresses': mail_list,
            },
            Message={
                'Body': {
                    'Text': {
                        'Charset': "UTF-8",
                        'Data': body,
                    },
                },
                'Subject': {
                    'Charset': "UTF-8",
                    'Data': subject,
                },
            },
            Source=settings.from_mail
        )
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        print("Email sent! Message ID:"),
        print(response['MessageId'])


def send_email_html(subject, body, to_email, html_message):
    mail_list = []
    if isinstance(to_email, list):
        for email in to_email:
            if is_valid_email_id(email):
                mail_list.append(email)
    else:
        if not is_valid_email_id(to_email):
            return
        if User.objects.filter(email=to_email) and check_if_user_is_dnd(User.objects.filter(email=to_email).first()):
            return
        mail_list = to_email
    client = boto3.client('ses', region_name=settings.AWS_REGION)
    try:
        response = client.send_email(
            Destination={
                'ToAddresses': mail_list,
            },
            Message={
                'Body': {
                    'Html': {
                        'Charset': "UTF-8",
                        'Data': html_message,
                    },
                    'Text': {
                        'Charset': "UTF-8",
                        'Data': body,
                    },
                },
                'Subject': {
                    'Charset': "UTF-8",
                    'Data': subject,
                },
            },
            Source=settings.from_mail
        )
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        print("Email sent! Message ID:"),
        print(response['MessageId'])
