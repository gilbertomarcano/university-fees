from django.db import models
from course.models import Course, CoursesChoices

# Create your models here.
# We create a model for class grade tracking
class Grade(models.Model):
    # this should be a foreign key to a student model
    # we should change this to student_id
    student_id = models.IntegerField()
    # term
    term = models.IntegerField(default=0)
    # this should be a foreign key to a course model
    # we should change this to course_id
    course_id = models.IntegerField(default=0)
    grade = models.FloatField()

    def __str__(self):
        # we get the course id and print it
        # we return the string

        return f"student_id: {self.student_id}, term: {self.term}, course_id: {self.course_id}, grade: {self.grade}"
