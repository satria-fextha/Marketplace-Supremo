from django import forms

class PagoForm(forms.Form):
    metodo_pago = forms.ChoiceField(choices=[('paypal', 'PayPal'), ('tarjeta', 'Tarjeta de crédito/débito')])
    monto = forms.DecimalField()
    factura = forms.FileField()
    comision = forms.DecimalField()
