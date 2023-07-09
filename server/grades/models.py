from django.db import models

# Create your models here.
# We create a model for class grade tracking
class Grade(models.Model):
    # this should be a foreign key to a student model
    student = models.CharField(max_length=10)
    # this should be a foreign key to a course model
    course = models.CharField(max_length=10)
    grade = models.FloatField()
