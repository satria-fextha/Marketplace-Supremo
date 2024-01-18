Funcionalidades/reviews/urls.py
from django.urls import path
from . import views
from django.urls import path
from . import views

app_name = 'payment'

urlpatterns = [
    path('process/', views.payment_process, name='process'),
    path('done/', views.payment_done, name='done'),
    path('canceled/', views.payment_canceled, name='canceled'),
    path('integrate/', views.integrate_payment_gateway, name='integrate'),
    path('charge/', views.charge_commissions, name='charge'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('products/<int:product_id>/rate/', views.calificar_producto, name='calificar_producto'),
    path('vendors/<int:vendedor_id>/rate/', views.calificar_vendedor, name='calificar_vendedor'),
    path('reviews/write/<int:product_id>/', views.escribir_resena, name='escribir_resena'),
    path('reviews/report/<int:resena_id>/', views.reportar_resena, name='reportar_resena'),
]
