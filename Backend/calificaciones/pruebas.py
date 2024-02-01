from django.db import models
from django.contrib.auth.models import User

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    # Otros campos del producto

class Vendedor(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    # Otros campos del vendedor

class Calificacion(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    puntuacion = models.IntegerField()
    comentario = models.TextField()
    aprobada = models.BooleanField(default=False)

class Resena(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    vendedor = models.ForeignKey(Vendedor, on_delete=models.CASCADE)
    comentario = models.TextField()
    aprobada = models.BooleanField(default=False)
