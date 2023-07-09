from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:student_id>", views.student_grades, name="student_grades"),
    path("<int:student_id>/<int:term>", views.student_term_grades, name="student_term_grades"),
    path("general-report/<int:student_id>", views.student_general_report, name="student_general_report")

]
