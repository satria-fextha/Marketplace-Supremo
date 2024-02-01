from django.db import models

class MetodoPago(models.Model):
    nombre = models.CharField(max_length=100)
    # Agregar otros campos necesarios para el método de pago

class Transaccion(models.Model):
    metodo_pago = models.ForeignKey(MetodoPago, on_delete=models.CASCADE)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    fecha = models.DateTimeField(auto_now_add=True)
    # Agregar otros campos necesarios para la transacción

class Factura(models.Model):
    transaccion = models.OneToOneField(Transaccion, on_delete=models.CASCADE)
    # Agregar otros campos necesarios para la factura

class Comision(models.Model):
    transaccion = models.OneToOneField(Transaccion, on_delete=models.CASCADE)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    # Agregar otros campos necesarios para la comisión
