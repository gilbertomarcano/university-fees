from django.db import models

# Create your models here.
# We create a model for class grade tracking
class Grade(models.Model):
    # this should be a foreign key to a student model
    # we should change this to studentId
    student = models.IntegerField()
    # term
    term = models.IntegerField(default=0)
    # this should be a foreign key to a course model
    # we should change this to courseId
    course = models.IntegerField()
    grade = models.FloatField()

    def __str__(self):
        return f"{self.student}, {self.course}, {self.grade}"
