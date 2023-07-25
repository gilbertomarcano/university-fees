from django.db import models

# Create your models here.

class Career(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Subject(models.Model):
    career = models.ForeignKey(Career, on_delete=models.CASCADE)
    semester = models.PositiveIntegerField()
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10, unique=True)
    prerequisites = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
