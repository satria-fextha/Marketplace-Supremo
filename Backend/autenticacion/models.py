from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models

class Agricultor(AbstractUser):
    # Atributos específicos para agricultores
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    # ...

class Ganadero(AbstractUser):
    # Atributos específicos para ganaderos
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    # ...

class Consumidor(AbstractUser):
    # Atributos específicos para consumidores
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    # ...


# Create your models here.
