from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse

class Driver(models.Model):
    name = models.CharField(max_length=128)

class Manufacturer(models.Model):
    name = models.CharField(verbose_name='Nome',max_length=30, unique=True)
    def __str__(self):
        return self.name

class Vehicle(models.Model):
    name = models.CharField(verbose_name='Nome',max_length=30)
    manufacturer = models.ForeignKey(Manufacturer,on_delete=models.CASCADE)
    description = models.TextField(verbose_name='Descrição',null=True, blank=True)
    licence_plate = models.CharField(verbose_name='Placa',max_length=7)
    manufacture_year = models.DateField(verbose_name='Ano de fabricação')
    is_activate = models.BooleanField(verbose_name='Ativo', default=True)
    usecontrols = models.ManyToManyField(Driver, through='UseControl')

    def get_absolute_url(self):
        return reverse('vehicle_list')

class UseControl(models.Model):
    driver = models.ForeignKey(Driver)
    vehicle = models.ForeignKey(Vehicle)
    date_started = models.DateTimeField(auto_now_add=True)
    date_ended = models.DateTimeField(blank=True, null=True)

class Manager(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, primary_key=True)
    name = models.CharField(max_length=30)
