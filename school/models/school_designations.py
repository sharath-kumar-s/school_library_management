from django.db import models
from common.models.base_model import BaseModel
from school.models.school_departments import SchoolDepartments
from school.models.school_model import School


class SchoolDesignations(BaseModel):
    school = models.ForeignKey(School, models.CASCADE)
    department = models.ForeignKey(SchoolDepartments, models.CASCADE)
    designation_name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = "school_designations"
        ordering = ['-created_at']
