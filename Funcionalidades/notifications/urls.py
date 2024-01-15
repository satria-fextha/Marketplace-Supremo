Funcionalidades/notifications/urls.py
from django.urls import path

from . import views

from django.urls import path

from . import views

urlpatterns = [
    path('notifications/', views.notifications, name='notifications'),
    path('generate_notification/<str:event_type>/<str:message>/', views.generate_notification, name='generate_notification'),
    path('manage_notifications/', views.manage_notifications, name='manage_notifications'),
]
    # Route for notifications page
    path('notifications/', views.notifications, name='notifications'),
    # Add more routes for other notification-related functionality if needed
]

from . import views

urlpatterns = [
    # Rutas de la interfaz de usuario
    path('', views.notifications, name='notifications'),
]
