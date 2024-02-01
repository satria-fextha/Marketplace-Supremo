from django.urls import path
from . import views

urlpatterns = [
    path('agregar/', views.agregar_producto, name='agregar_producto'),
    path('actualizar/', views.actualizar_producto, name='actualizar_producto'),
    path('eliminar/', views.eliminar_producto, name='eliminar_producto'),
]
