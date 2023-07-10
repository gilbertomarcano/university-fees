from django.db import models

# Create your models here.
# WE FILL THIS with course names and ids
class CoursesChoices(models.TextChoices):
    CHEMISTRYI = "QI", "QuímicaI"
    PHYSICS = "F", "Física"
    MATHI = "M1", "Matemática 1"
    MATHII = "M2", "Matemática 2"
    MATHIII = "M3", "Matemática 3"
    MATHIV = "M4", "Matemática 4"
    PROGRAMACIONAVANZADA = "PA", "Programación Avanzada"
    PROGRAMACIONLINEAL = "PL", "Programación Lineal"
    DESARROLLOAVANZADO = "DA", "Desarrollo Avanzado"
    TALLERDESARROLLOAVANZADO = "TDA", "Taller de Desarrollo Avanzado"
    TALLERPROGRAMACIONAVANZADA = "TPA", "Taller de Programación Avanzada"
    TALLERPROGRAMACIONLINEAL = "TPL", "Taller de Programación Lineal"

class Course(models.Model):
    course_id = models.CharField(max_length=10, primary_key=True)
    course_name = models.CharField(max_length=32, choices=CoursesChoices.choices)

    def __str__(self):
        course_name = ""
         
        for course in CoursesChoices.choices:
            if course[0] == self.course_name:
                course_name = course[1]
                break

        return f"{self.course_id}: {self.course_name}, {course_name}"
    
    def get_name_enum_value(self):
        course_name = ""
         
        for course in CoursesChoices.choices:
            if course[0] == self.course_name:
                course_name = course[1]
                break

        return course_name