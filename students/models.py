from django.db import models

class Student(models.Model):
    student_id = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    department = models.CharField(max_length=50)
    attendance = models.FloatField()
    python_score = models.FloatField()
    sql_score = models.FloatField()
    ml_score = models.FloatField()
    final_mark = models.FloatField()

    def __str__(self):
        return self.name
        
    @property
    def performance_status(self):
        if self.final_mark >= 90:
            return "Excellent"
        elif self.final_mark >= 75:
            return "Good"
        else:
            return "Needs Improvement"
