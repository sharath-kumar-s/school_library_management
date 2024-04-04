from django.db import models
from common.models.base_model import BaseModel
from employees.models.employee_basic_details_model import Employees
from school.models.school_classes import SchoolClassSections, SchoolClasses
from school.models.school_libraries import SchoolLibraries
from school.models.school_library_books import SchoolLibraryBooks
from school.models.school_model import School
from school.models.school_students import SchoolStudents
from school.models.school_subjects import SchoolClassSubjects


class SchoolStudentsBookBorrowRecord(BaseModel):
    school = models.ForeignKey(School, models.CASCADE)
    school_library = models.ForeignKey(SchoolLibraries, models.CASCADE)
    class_name = models.ForeignKey(SchoolClasses, models.CASCADE)
    section_name = models.ForeignKey(SchoolClassSections, models.CASCADE)
    subject_name = models.ForeignKey(SchoolClassSubjects, models.CASCADE)
    student_id = models.ForeignKey(SchoolStudents, models.CASCADE)
    borrowed_book = models.ForeignKey(SchoolLibraryBooks, models.CASCADE)
    book_given_employee = models.ForeignKey(Employees, models.CASCADE, related_name='book_given_librarian')
    book_collected_employee = models.ForeignKey(Employees, models.CASCADE, related_name='book_collected_librarian')
    borrow_date = models.DateField()
    date_to_return = models.DateField()
    renewal_status = models.CharField(max_length=255, default=False)  # True, False
    renewed_date = models.DateField(null=True)
    book_return_status = models.CharField(max_length=255, default='Not returned')  # Returned, Not returned
    returned_datetime = models.DateTimeField()
    comment = models.CharField(max_length=500, blank=True)

    class Meta:
        db_table = "students_book_borrowing_record"
        ordering = ['-created_at']
