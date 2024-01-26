from django.contrib.auth.models import AbstractUser
from django.db import models

class Agricultor(AbstractUser):
    # Atributos específicos del agricultor
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)

class Ganadero(AbstractUser):
    # Atributos específicos del ganadero
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)

class Consumidor(AbstractUser):
    # Atributos específicos del consumidor
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)

# Implementar funciones CRUD para cada modelo de usuario

# Implementar autenticación por correo electrónico o número de teléfono y contraseña

# Utilizar una biblioteca de autenticación segura para almacenar las contraseñas de manera segura

# Implementar la lógica para verificar la autenticidad de los correos electrónicos o números de teléfono

# Desarrollar la lógica de selección de tipo de usuario y enviar correos o SMS de verificación

# Crear una interfaz de usuario para seleccionar el tipo de usuario durante el registro

# Implementar la lógica para enviar correos electrónicos o SMS de verificación después del registro
