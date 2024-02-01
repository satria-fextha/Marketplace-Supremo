from django import forms
from .models import Producto, Vendedor, Calificacion, Resena

class CalificacionForm(forms.ModelForm):
    class Meta:
        model = Calificacion
        fields = ['producto', 'puntuacion']

class ResenaForm(forms.ModelForm):
    class Meta:
        model = Resena
        fields = ['producto', 'vendedor', 'contenido']

class ModeracionForm(forms.ModelForm):
    class Meta:
        model = Resena
        fields = ['aprobada']
