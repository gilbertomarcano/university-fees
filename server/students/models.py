from django.db import models

from users.models import User

# Create your models here.
class NationalIdPrefixChoices(models.TextChoices):
    V = 'V', 'Venezolano'
    E = 'E', 'Extranjero'


class CareerChoices(models.TextChoices):
    COMPUTER_ENGINEERING = 'computer_engineering', 'Ingenieria En Computacion'
    SYSTEMS_ENGINEERING = 'systems_engineering', 'Ingenieria De Sistemas'
    ELECTRICAL_ENGINEERING = 'electrical_engineering', 'Ingenieria Electrica'
    PETROLEUM_ENGINEERING = 'petroleum_engineering', 'Ingeniería De Petróleo'
    INDUSTRIAL_ENGINEERING = 'industrial_engineering', 'Ingeniería Industrial'
    CIVIL_ENGINEERING = 'civil_engineering', 'Ingeniería Civil' 
    MECHANICAL_ENGINEERING = 'mechanical_engineering', 'Ingeniería Mecánica'
    CHEMICAL_ENGINEERING = 'chemical_engineering', 'Ingeniería Química'
    ARCHITECTURE = 'architecture', 'Arquitectura'
    MEDICINE = 'medicine', 'Medicina'
    ACCOUNTING = 'accounting', 'Contaduría'
    BUSINESS_ADMINISTRATION = 'business_administration', 'Administración'


class GenderChoices(models.TextChoices):
    MALE = 'M', 'Masculino'
    FEMALE = 'F', 'Femenino'
    OTHER = 'O', 'Otro'


class VenezuelanRegionChoices(models.TextChoices):
    AMAZONAS = 'AM', 'Amazonas'
    ANZOATEGUI = 'AN', 'Anzoátegui'
    APURE = 'AP', 'Apure'
    ARAGUA = 'AR', 'Aragua'
    BARINAS = 'BA', 'Barinas'
    BOLIVAR = 'BO', 'Bolívar'
    CARABOBO = 'CA', 'Carabobo'
    COJEDES = 'CO', 'Cojedes'
    DELTA_AMACURO = 'DE', 'Delta Amacuro'
    DISTRITO_CAPITAL = 'DC', 'Distrito Capital'
    FALCON = 'FA', 'Falcón'
    GUARICO = 'GU', 'Guárico'
    LARA = 'LA', 'Lara'
    MERIDA = 'ME', 'Mérida'
    MIRANDA = 'MI', 'Miranda'
    MONAGAS = 'MO', 'Monagas'
    NUEVA_ESPARTA = 'NE', 'Nueva Esparta'
    PORTUGUESA = 'PR', 'Portuguesa'
    SUCRE = 'SU', 'Sucre'
    TACHIRA = 'TA', 'Táchira'
    TRUJILLO = 'TR', 'Trujillo'
    VARGAS = 'VA', 'Vargas'
    YARACUY = 'YA', 'Yaracuy'
    ZULIA = 'ZU', 'Zulia'


class Student(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)
    career = models.CharField(max_length=32, choices=CareerChoices.choices)
    region = models.CharField(max_length=32, choices=VenezuelanRegionChoices.choices)
    national_id_prefix = models.CharField(max_length=1, choices=NationalIdPrefixChoices.choices)
    national_id_number = models.CharField(max_length=10)
    gender = models.CharField(max_length=10, choices=GenderChoices.choices)

