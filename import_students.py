import csv
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dashboard.settings")
django.setup()

from students.models import Student

with open("data/students.csv", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        Student.objects.create(
            student_id=row["Student_ID"],
            name=row["Name"],
            gender=row["Gender"],
            department=row["Department"],
            attendance=float(row["Attendance"]),
            python_score=float(row["Python"]),
            sql_score=float(row["SQL"]),
            ml_score=float(row["ML"]),
            final_mark=float(row["Final_Mark"])
        )

print("Students imported successfully!")