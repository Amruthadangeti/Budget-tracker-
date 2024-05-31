from django.db import models

# Create your models here.


class Envelope(models.Model):
    name = models.CharField(max_length=100)
    budget_amount = models.PositiveIntegerField(default=1)
    current_balance = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.name

