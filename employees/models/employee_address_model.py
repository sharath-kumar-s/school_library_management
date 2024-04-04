from django.db import models
from common.models.base_model import BaseMetaModel
from employees.models.employee_basic_details_model import Employees
from school.models.school_model import School


class SchoolEmployeesAddress(BaseMetaModel):
    school = models.ForeignKey(School, models.CASCADE)
    employee_id = models.ForeignKey(Employees, on_delete=models.CASCADE)
    address_type = models.CharField(max_length=500)
    full_address = models.CharField(max_length=500)
    land_mark = models.CharField(max_length=500)
    city = models.CharField(max_length=500)
    state = models.CharField(max_length=500)
    pincode = models.IntegerField(max_length=500)

    class Meta:
        db_table = 'school_employees_address'
