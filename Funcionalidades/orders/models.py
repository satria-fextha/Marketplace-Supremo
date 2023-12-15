from django.db import models
from django.contrib.auth.models import User
from products.models import Product

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
