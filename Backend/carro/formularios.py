from django import forms
from .models import Producto

class AgregarProductoForm(forms.Form):
    producto_id = forms.IntegerField()
    cantidad = forms.IntegerField()

    def clean_producto_id(self):
        producto_id = self.cleaned_data['producto_id']
        try:
            producto = Producto.objects.get(id=producto_id)
        except Producto.DoesNotExist:
            raise forms.ValidationError("El producto no existe")
        return producto_id

class ActualizarCantidadForm(forms.Form):
    producto_id = forms.IntegerField()
    cantidad = forms.IntegerField()

    def clean_producto_id(self):
        producto_id = self.cleaned_data['producto_id']
        try:
            producto = Producto.objects.get(id=producto_id)
        except Producto.DoesNotExist:
            raise forms.ValidationError("El producto no existe")
        return producto_id

class EliminarProductoForm(forms.Form):
    producto_id = forms.IntegerField()

    def clean_producto_id(self):
        producto_id = self.cleaned_data['producto_id']
        try:
            producto = Producto.objects.get(id=producto_id)
        except Producto.DoesNotExist:
            raise forms.ValidationError("El producto no existe")
        return producto_id
