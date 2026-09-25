from django.contrib import admin

from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = (
        "student_id",
        "name",
        "gender",
        "department",
        "attendance",
        "python_score",
        "sql_score",
        "ml_score",
        "final_mark",
    )
