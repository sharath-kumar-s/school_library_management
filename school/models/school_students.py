from django.db import models
from common.models.base_model import BaseModel
from school.models.school_classes import SchoolClassSections, SchoolClasses
from school.models.school_model import School


class SchoolStudents(BaseModel):
    school = models.ForeignKey(School, models.CASCADE)
    class_name = models.ForeignKey(SchoolClasses, models.CASCADE)
    section_name = models.ForeignKey(SchoolClassSections, models.CASCADE)
    student_first_name = models.CharField(max_length=255)
    student_last_name = models.CharField(max_length=255)
    gender = models.CharField(max_length=255)
    date_of_joining = models.CharField(max_length=255)
    email_id = models.EmailField(max_length=255, blank=True)
    photo = models.ImageField(upload_to='school/student/profile', max_length=255)
    father_name = models.CharField(max_length=255)
    father_mobile_number = models.BigIntegerField(max_length=255)
    mother_name = models.CharField(max_length=255)
    mother_mobile_number = models.BigIntegerField(max_length=255)
    status = models.CharField(max_length=255, default='Pending')  # Pending, Approved, Rejected, Terminated
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = "school_students"
        ordering = ['-created_at']


class SchoolStudentsLogin(BaseModel):
    school = models.ForeignKey(School, models.CASCADE)
    student_id = models.ForeignKey(SchoolStudents, models.CASCADE)
    password = models.CharField(max_length=500)
    last_login = models.DateTimeField(null=True, default=None)
    email_otp = models.CharField(max_length=10, blank=True, null=True)
    mobile_otp = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        db_table = "school_student_login"
        ordering = ['-created_at']
