from django.db import models

# Create your models here.
from django.db import models


class Project(models.Model):   
    name = models.CharField(max_length=100)
    description = models.PositiveIntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

