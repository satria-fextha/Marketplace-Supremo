from django import forms
from .models import Agricultor, Ganadero, Consumidor

class AgricultorForm(forms.ModelForm):
    class Meta:
        model = Agricultor
        fields = '__all__'

class GanaderoForm(forms.ModelForm):
    class Meta:
        model = Ganadero
        fields = '__all__'

class ConsumidorForm(forms.ModelForm):
    class Meta:
        model = Consumidor
        fields = '__all__'
