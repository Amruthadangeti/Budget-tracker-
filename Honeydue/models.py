from django.db import models

# Create your models here.
from django.db import models


class Project(models.Model):
    
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return self.name

