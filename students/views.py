from django.shortcuts import render, get_object_or_404
from django.db.models import Avg, Max
from .models import Student


def dashboard(request):
    search = request.GET.get("search", "")

    students = Student.objects.all()

    if search:
        students = students.filter(name__icontains=search)

    total_students = students.count()

    average_mark = students.aggregate(
        Avg("final_mark")
    )["final_mark__avg"]

    average_attendance = students.aggregate(
        Avg("attendance")
    )["attendance__avg"]

    highest_mark = students.aggregate(
        Max("final_mark")
    )["final_mark__max"]

    top_student = students.order_by("-final_mark").first()

    python_average = students.aggregate(
        Avg("python_score")
    )["python_score__avg"]

    sql_average = students.aggregate(
        Avg("sql_score")
    )["sql_score__avg"]

    ml_average = students.aggregate(
        Avg("ml_score")
    )["ml_score__avg"]

    correlation = students.values_list(
        "attendance",
        "final_mark"
    )
    correlation = list(correlation)

    n = len(correlation)

    if n > 1:
        attendance_values = [row[0] for row in correlation]
        mark_values = [row[1] for row in correlation]

        attendance_mean = sum(attendance_values) / n
        mark_mean = sum(mark_values) / n

        numerator = sum(
            (attendance_values[i] - attendance_mean) *
            (mark_values[i] - mark_mean)
            for i in range(n)
        )

        attendance_variance = sum(
            (x - attendance_mean) ** 2
            for x in attendance_values
        )

        mark_variance = sum(
            (y - mark_mean) ** 2
            for y in mark_values
        )

        correlation_value = numerator / (
            attendance_variance * mark_variance
        ) ** 0.5
    else:
        correlation_value = 0

    context = {
        "students": students,
        "total_students": total_students,
        "average_mark": round(average_mark, 2),
        "average_attendance": round(average_attendance, 2),
        "highest_mark": highest_mark,
        "top_student": top_student,
        "python_average": round(python_average, 2),
        "sql_average": round(sql_average, 2),
        "ml_average": round(ml_average, 2),
        "correlation_value": round(correlation_value, 2),
    }

    return render(request, "students/dashboard.html", context)


def student_detail(request, student_id):
    student = get_object_or_404(Student, id=student_id)

    return render(
        request,
        "students/student_detail.html",
        {"student": student}
    )