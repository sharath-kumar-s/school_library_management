from django.db import models
from common.models.base_model import BaseModel
from school.models.school_model import School


class SchoolLibraries(BaseModel):
    school = models.ForeignKey(School, models.CASCADE)
    library_name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = "school_departments"
        ordering = ['-created_at']
