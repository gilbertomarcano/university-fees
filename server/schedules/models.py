from django.db import models

# Create your models here.

class Professor(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Schedule(models.Model):
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    day = models.CharField(max_length=10, choices=[('Mon', 'Monday'), ('Tue', 'Tuesday'), ('Wed', 'Wednesday'), ('Thu', 'Thursday'), ('Fri', 'Friday')])
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"{self.professor} - {self.course} ({self.day} {self.start_time}-{self.end_time})"
