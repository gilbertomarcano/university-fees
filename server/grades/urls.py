from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:studentId>", views.student_grades, name="student_grades"),
    path("<int:studentId>/<int:term>", views.student_term_grades, name="student_term_grades")
]
