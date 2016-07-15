from django.db import models

class Vehicle(models.Model):

    name = models.CharField(max_length=30)
    description = models.TextField(null=True, blank=True)
