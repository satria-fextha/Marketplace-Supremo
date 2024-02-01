from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class AgricultorForm(UserCreationForm):
    # Define the necessary attributes for the Agricultor model
    # ...

class GanaderoForm(UserCreationForm):
    # Define the necessary attributes for the Ganadero model
    # ...

class ConsumidorForm(UserCreationForm):
    # Define the necessary attributes for the Consumidor model
    # ...
