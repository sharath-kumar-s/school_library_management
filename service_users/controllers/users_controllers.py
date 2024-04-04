from common.helpers.custom_messages import *
from common.helpers.responses import response_messages
from common.helpers.save_to_s3 import save_base64_to_public_s3_get_url
from school_management import settings
from service_users.models import ServiceUsers
import time


class ServiceUserDetailsController(object):

    def __init__(self, data, user_in_context, *args, **kwargs):
        self.data = data
        self.user_in_context = user_in_context

    def service_user_details(self):
        result = {
            "message": response_messages.ACCOUNT_CREATED,
            "status": "success"
        }

        fields = [
            'title', 'full_name', 'middle_name', 'last_name', 'user_name', 'user_id', 'mobile_country_code', 'gender',
            'mobile_number', 'user_photo', 'user_photo_extension', 'email_id', 'date_of_birth', 'identification_type',
            'identification_number', 'identification_photo', 'identification_photo_extension'
        ]

        if all(item in self.data.keys() for item in fields) is False:
            for field in fields:
                if field not in self.data.keys():
                    result['message'] = field + " missing in request body"
                    result['status'] = False
                    return result
        # user = User.objects.filter()

        if ServiceUsers.objects.filter(email_id=self.data.get('email_id')).exists():
            result['message'] = response_messages.USER_EXISTS
            result['status'] = False
            return result

        s3_bucket_name = settings.KV_IMAGES_BUCKET
        file_name = 'user_image_' + time.strftime("%Y%m%d%H%M%S") + "." + self.data.get('user_photo_extension')
        file_url = save_base64_to_public_s3_get_url(
            s3_bucket_name,
            file_name,
            self.data.get('user_photo')
        )

        doc_file_name = 'user_doc_image_' + time.strftime("%Y%m%d%H%M%S") + "." + self.data.get('identification_photo_extension')
        doc_file_url = save_base64_to_public_s3_get_url(
            s3_bucket_name,
            doc_file_name,
            self.data.get('identification_photo')
        )

        # users = ServiceUsers.objects.get(id=self.data.get('user_id'))
        service_user = ServiceUsers(
            title=self.data.get('title'),
            full_name=self.data.get('full_name'),
            middle_name=self.data.get('middle_name'),
            last_name=self.data.get('last_name'),
            user_name=self.data.get('user_name'),
            user_id=self.data.get('user_id'),
            mobile_country_code=self.data.get('mobile_country_code'),
            mobile_number=self.data.get('mobile_number'),
            gender=self.data.get('gender'),
            email_id=self.data.get('email_id'),
            date_of_birth=self.data.get('date_of_birth'),
            identification_type=self.data.get('identification_type'),
            identification_number=self.data.get('identification_number'),
            status=self.data.get('status'),
            user_photo=file_url,
            identification_photo=doc_file_url)

        service_user.save()
        return result
