from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Account(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='accounts')
    name = models.CharField(max_length=100)
    balance = models.DecimalField(max_digits=10, decimal_places=2)

    def _str_(self):
        return f"{self.name} ({self.user.username})"


