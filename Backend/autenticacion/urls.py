from django.urls import path
from . import views

urlpatterns = [
    path('registro/agricultor/', views.registro_agricultor, name='registro_agricultor'),
    path('registro/ganadero/', views.registro_ganadero, name='registro_ganadero'),
    path('registro/consumidor/', views.registro_consumidor, name='registro_consumidor'),
    # Add other URL patterns for CRUD operations and authentication
    path('registro/', views.registro, name='registro'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('perfil/', views.perfil, name='perfil'),
    path('editar-perfil/', views.editar_perfil, name='editar_perfil'),
    path('eliminar-perfil/', views.eliminar_perfil, name='eliminar_perfil'),
]
