from django.db import models
from django.contrib.auth.models import User
from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    categoria = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    ubicacion = models.CharField(max_length=100)
    agricultor = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
