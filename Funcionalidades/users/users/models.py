
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_user(self, email_or_phone, password=None, **extra_fields):
        if not email_or_phone:
            raise ValueError('El correo electrónico o número de teléfono es obligatorio')
        user = self.model(email_or_phone=email_or_phone, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email_or_phone, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email_or_phone, password, **extra_fields)

class CustomUser(AbstractBaseUser):
    FARMER = 'farmer'
    LIVESTOCK_FARMER = 'livestock_farmer'
    CONSUMER = 'consumer'
    USER_TYPE_CHOICES = [
        (FARMER, 'Agricultor'),
        (LIVESTOCK_FARMER, 'Ganadero'),
        (CONSUMER, 'Consumidor'),
    ]
    email_or_phone = models.CharField(max_length=255, unique=True)
    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email_or_phone'

    objects = CustomUserManager()

    def __str__(self):
        return self.email_or_phone

class FarmerProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='farmer_profile')
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    contact = models.CharField(max_length=255)
    products = models.TextField()
    history = models.TextField()
    certifications = models.TextField()

class LivestockFarmerProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='livestock_farmer_profile')
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    contact = models.CharField(max_length=255)
    products = models.TextField()
    history = models.TextField()
    certifications = models.TextField()

class ConsumerProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='consumer_profile')
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    contact = models.CharField(max_length=255)
    purchase_history = models.TextField()
    preferences = models.TextField()
    wishlist = models.TextField()
