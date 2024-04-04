from django.db import models
from common.models.base_model import BaseModel
from school.models.school_model import School


class SchoolClasses(BaseModel):
    school = models.ForeignKey(School, models.CASCADE)
    class_name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = "school_classes"
        ordering = ['-created_at']


class SchoolClassSections(BaseModel):
    school = models.ForeignKey(School, models.CASCADE)
    class_name = models.ForeignKey(SchoolClasses, models.CASCADE)
    section_name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = "school_sections"
        ordering = ['-created_at']
