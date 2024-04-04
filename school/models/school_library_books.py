from django.db import models
from common.models.base_model import BaseModel
from school.models.school_classes import SchoolClassSections, SchoolClasses
from school.models.school_libraries import SchoolLibraries
from school.models.school_model import School
from school.models.school_subjects import SchoolClassSubjects


class SchoolLibraryBooks(BaseModel):
    school = models.ForeignKey(School, models.CASCADE)
    school_library = models.ForeignKey(SchoolLibraries, models.CASCADE)
    class_name = models.ForeignKey(SchoolClasses, models.CASCADE)
    section_name = models.ForeignKey(SchoolClassSections, models.CASCADE)
    subject_name = models.ForeignKey(SchoolClassSubjects, models.CASCADE)
    book_title = models.CharField(max_length=255)
    book_author = models.CharField(max_length=255)
    purchased_on = models.DateField()
    description = models.CharField(max_length=255, blank=True)
    total_number_of_books = models.IntegerField()
    number_of_books_borrowed = models.IntegerField()
    number_of_books_available = models.IntegerField()
    book_available_date = models.DateField()
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = "school_library_books"
        ordering = ['-created_at']
