from django.db import models

# Create your models here.
from django.db import models

class Account(models.Model):
    name = models.CharField(max_length=100)
    balance = models.DecimalField(max_digits=10, decimal_places=2)

    def _str_(self):
        return f"{self.name} ({self.user.username})"


