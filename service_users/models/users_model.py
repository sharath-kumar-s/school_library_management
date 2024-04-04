from django.db import models
from django.contrib.auth.models import User
from school_management.common.models.base_model import BaseMetaModel


class ServiceUsers(BaseMetaModel):
    """These are application service master admin users"""
    user = models.OneToOneField(User, models.DO_NOTHING)
    title = models.CharField(max_length=20, blank=True, null=True)
    full_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255)
    user_name = models.CharField(max_length=50)
    user_id = models.CharField(max_length=50, blank=True, null=True)
    mobile_country_code = models.CharField(max_length=10)
    mobile_number = models.BigIntegerField(max_length=20)
    gender = models.CharField(max_length=20)
    user_photo = models.CharField(max_length=500)
    email_id = models.EmailField(max_length=100, unique=True)
    date_of_birth = models.DateField(blank=True, null=True)
    identification_type = models.CharField(max_length=50)
    identification_number = models.CharField(max_length=50)
    identification_photo = models.CharField(max_length=500, blank=True, null=True)
    status = models.CharField(max_length=20, default='Active')  # Active, Inactive, Hold, Blocked, Terminated

    class Meta:
        db_table = 'service_users'
        ordering = ['-created_at']


class ServiceUsersLogin(BaseMetaModel):
    user_id = models.ForeignKey(ServiceUsers, on_delete=models.CASCADE)
    password = models.CharField(max_length=500)
    last_login = models.DateTimeField(null=True, default=None)
    email_otp = models.CharField(max_length=10, blank=True, null=True)
    mobile_otp = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        db_table = 'service_users_login'
