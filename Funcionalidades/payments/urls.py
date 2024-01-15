from django.urls import path

from . import views

app_name = 'payments'

urlpatterns = [
    path('', views.payment_process, name='payment_process'),
    path('done/', views.payment_done, name='payment_done'),
    path('canceled/', views.payment_canceled, name='payment_canceled'),
    path('integrate/', views.integrate_payment_gateway, name='integrate_payment_gateway'),
    path('charge/', views.charge_commissions, name='charge_commissions'),
]
from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('payments/', views.payments_home, name='payments_home'),
    path('payments/process/', views.payment_process, name='payment_process'),
    path('payments/done/', views.payment_done, name='payment_done'),
    path('payments/canceled/', views.payment_canceled, name='payment_canceled'),
]
