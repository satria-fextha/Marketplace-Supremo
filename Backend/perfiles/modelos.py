from django.db import models

class Agricultor(models.Model):
    nombre = models.CharField(max_length=100)
    edad = models.IntegerField()
    direccion = models.CharField(max_length=200)
    # Agrega aquí los atributos específicos para el perfil de agricultor

class Ganadero(models.Model):
    nombre = models.CharField(max_length=100)
    edad = models.IntegerField()
    direccion = models.CharField(max_length=200)
    # Agrega aquí los atributos específicos para el perfil de ganadero

class Consumidor(models.Model):
    nombre = models.CharField(max_length=100)
    edad = models.IntegerField()
    direccion = models.CharField(max_length=200)
    # Agrega aquí los atributos específicos para el perfil de consumidor
