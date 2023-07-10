from django.db import models

from students.models import Student

# Create your models here.
# We create a model for class grade tracking
class Grade(models.Model):
    # this should be a foreign key to a student model
    # we should change this to student_id
    student = models.ForeignKey(to=Student, on_delete=models.CASCADE)
    # student_id = models.IntegerField()
    # term
    term = models.IntegerField(default=0)
    # this should be a foreign key to a course model
    # we should change this to course_id
    course_id = models.IntegerField()
    grade = models.FloatField()

    def __str__(self):
        return f"student_id: {self.student_id}, term: {self.term}, course_id: {self.course_id}, grade: {self.grade}"
