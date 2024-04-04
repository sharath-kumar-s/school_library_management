from django.db import models
from common.models.base_model import BaseModel
from school.models.school_libraries import SchoolLibraries
from school.models.school_model import School


class SchoolLibraryConfiguaration(BaseModel):
    school = models.ForeignKey(School, models.CASCADE)
    school_library = models.ForeignKey(SchoolLibraries, models.CASCADE)
    book_borrow_count_student = models.IntegerField(default=10)
    book_return_days = models.IntegerField(default=30)
    book_renewal_times = models.IntegerField(default=1)
    renewal_days = models.IntegerField(default=30)
    renewal_grace_period = models.IntegerField(default=30)

    class Meta:
        db_table = "school_library_configuarations"
