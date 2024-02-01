from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import Farmer, LivestockOwner, Consumer

class Farmer(AbstractUser):
    farm_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

class LivestockOwner(AbstractUser):
    livestock_name = models.CharField(max_length=100)
    livestock_type = models.CharField(max_length=100)

class Consumer(AbstractUser):
    address = models.CharField(max_length=100)

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user_type = request.POST['user_type']
        
        if user_type == 'farmer':
            farm_name = request.POST['farm_name']
            location = request.POST['location']
            farmer = Farmer.objects.create_user(username=username, password=password, farm_name=farm_name, location=location)
            farmer.save()
        elif user_type == 'livestock_owner':
            livestock_name = request.POST['livestock_name']
            livestock_type = request.POST['livestock_type']
            livestock_owner = LivestockOwner.objects.create_user(username=username, password=password, livestock_name=livestock_name, livestock_type=livestock_type)
            livestock_owner.save()
        elif user_type == 'consumer':
            address = request.POST['address']
            consumer = Consumer.objects.create_user(username=username, password=password, address=address)
            consumer.save()
        
        return redirect('login')
    else:
        return render(request, 'register.html')
