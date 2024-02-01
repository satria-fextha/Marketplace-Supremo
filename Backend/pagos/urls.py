from django.urls import path
from . import views

urlpatterns = [
    path('pagar/paypal/', views.paypal_payment, name='paypal_payment'),
    path('pagar/tarjeta/', views.credit_card_payment, name='credit_card_payment'),
    # Add more payment method URLs here
]
