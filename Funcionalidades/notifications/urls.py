Funcionalidades/notifications/urls.py
from django.urls import path

from . import views

urlpatterns = [
    # Route for notifications page
    path('notifications/', views.notifications, name='notifications'),
    # Add more routes for other notification-related functionality if needed
]

from . import views

urlpatterns = [
    # Rutas de la interfaz de usuario
    path('', views.notifications, name='notifications'),
]
