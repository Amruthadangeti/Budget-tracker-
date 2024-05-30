from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Envelope(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    budget_amount = models.DecimalField(max_digits=10, decimal_places=2)
    current_balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def _str_(self):
        return f"{self.name} ({self.user.username})"

