from django.db import models
from common.models.base_model import BaseModel


class School(BaseModel):
    school_name = models.CharField(max_length=255)
    school_email = models.EmailField(max_length=255, blank=True)
    school_mobile = models.BigIntegerField(db_index=True)
    school_website = models.CharField(max_length=255)
    school_registration_number = models.CharField(max_length=255)
    school_city = models.CharField(max_length=255)
    school_state = models.CharField(max_length=255)
    school_address = models.CharField(max_length=255)
    school_country = models.CharField(max_length=255)
    school_pincode = models.CharField(max_length=255)

    class Meta:
        db_table = "school"
        ordering = ['-created_at']
