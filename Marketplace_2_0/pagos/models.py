from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)

class Order(models.Model):
    STATUS_CHOICES = (
        ('preparation', 'En preparación'),
        ('shipped', 'Enviado'),
        ('delivered', 'Entregado'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='preparation')
    created_at = models.DateTimeField(auto_now_add=True)


# Create your models here.
