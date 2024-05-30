from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Wallet(models.Model):
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    created_at = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return f"{self.user.username}'s Wallet"
