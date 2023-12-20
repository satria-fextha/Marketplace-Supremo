Funcionalidades/payments/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('payments/', views.payments_home, name='payments_home'),
    path('payments/process/', views.payment_process, name='payment_process'),
    path('payments/done/', views.payment_done, name='payment_done'),
    path('payments/canceled/', views.payment_canceled, name='payment_canceled'),
]
