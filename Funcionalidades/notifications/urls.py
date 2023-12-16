from django.urls import path

from . import views

urlpatterns = [
    # Rutas de la interfaz de usuario
    path('', views.notifications, name='notifications'),
]
