from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:studentId>", views.studentGrades, name="studentGrades"),
    path("<int:studentId>/<int:term>", views.studentTermGrades, name="studentTermGrades")
]
