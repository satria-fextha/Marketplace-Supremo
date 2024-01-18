Funcionalidades/orders/models.py
from django.db import models
from django.contrib.auth.models import User
from products.models import Product

class Order(models.Model):
    STATUS_CHOICES = (
        ('P', 'En preparación'),
        ('S', 'Enviado'),
        ('D', 'Entregado'),
        ('C', 'Cancelado'),
    )

    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    consumer = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through='OrderItem')
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='P')
    created_at = models.DateTimeField(auto_now_add=True)

    def accept_order(self):
        self.status = 'P'
        self.save()

    def reject_order(self):
        self.status = 'C'
        self.save()

    def update_status(self, new_status):
        self.status = new_status
        self.save()

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='order_items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def calculate_subtotal(self):
        return self.product.price * self.quantity

class ShoppingCart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through='CartItem')
    created_at = models.DateTimeField(auto_now_add=True)

    def calculate_total(self):
        return sum(item.product.price * item.quantity for item in self.cart_items.all())

class CartItem(models.Model):
    shopping_cart = models.ForeignKey(ShoppingCart, related_name='cart_items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def calculate_subtotal(self):
        return self.product.price * self.quantity
