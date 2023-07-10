from django.db import models
from users.models import User

# Create your models here.

class Payment(models.Model):
    date = models.DateField(auto_now_add=True)
    reference = models.CharField(max_length=128)
    description = models.CharField(max_length=128)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    balance = models.DecimalField(max_digits=8, decimal_places=2)
    user = models.ForeignKey(to = User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.reference