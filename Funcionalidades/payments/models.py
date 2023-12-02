
from django.db import models
from django.contrib.auth.models import User


class Payment(models.Model):
    PAYMENT_METHODS = (
        ('paypal', 'PayPal'),
        ('credit_card', 'Tarjeta de crédito'),
        ('debit_card', 'Tarjeta de débito'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateTimeField(auto_now_add=True)
    payment_method = models.CharField(max_length=50, choices=PAYMENT_METHODS)
    transaction_id = models.CharField(max_length=100)
    status = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.user.username} - {self.amount}"


class Invoice(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE)
    invoice_number = models.CharField(max_length=50)
    invoice_date = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField()
    status = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.user.username} - {self.invoice_number}"

class PaymentGateway(models.Model):
    name = models.CharField(max_length=50)
    logo = models.ImageField(upload_to='payment_gateways/')
    description = models.TextField()
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name


class PaymentTransaction(models.Model):
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE)
    payment_gateway = models.ForeignKey(PaymentGateway, on_delete=models.CASCADE)
    transaction_id = models.CharField(max_length=100)
    transaction_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.payment.user.username} - {self.payment.amount} - {self.payment_gateway.name}"


class InvoiceItem(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return self.name
