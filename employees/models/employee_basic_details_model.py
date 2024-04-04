from django.db import models
from django.contrib.auth.models import User
from common.models.base_model import BaseModel
from school.models.school_model import School


class Employees(BaseModel):
    user = models.OneToOneField(User, models.DO_NOTHING)
    school = models.ForeignKey(School, models.CASCADE)
    mobile_number = models.BigIntegerField(max_length=10)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email_id = models.EmailField(max_length=255, blank=True)
    employment_type = models.CharField(max_length=10)
    date_of_birth = models.DateField(max_length=10)
    date_of_joining = models.DateField(max_length=10)
    gender = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='school/employees/profile_photo', max_length=255)
    status = models.CharField(max_length=100, blank=True, null=True)  # Active, Inactive, Hold, Blocked, Terminated

    class Meta:
        db_table = "employees"
        ordering = ['-created_at']
