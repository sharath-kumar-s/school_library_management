from django.db import models
from common.models.base_model import BaseMetaModel
from employees.models.employee_basic_details_model import Employees


class SchoolEmployeesLogin(BaseMetaModel):
    employee_id = models.ForeignKey(Employees, on_delete=models.CASCADE)
    password = models.CharField(max_length=500)
    last_login = models.DateTimeField(null=True, default=None)
    email_otp = models.CharField(max_length=10, blank=True, null=True)
    mobile_otp = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        db_table = 'school_employees_login'
