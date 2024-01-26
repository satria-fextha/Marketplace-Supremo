from django.urls import path
from autenticacion import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    # Add more URLs for password reset, email/phone verification, etc.
    # Add URLs for CRUD operations for farmer, rancher, and consumer models
    path('farmer/create/', views.create_farmer, name='create_farmer'),
    path('farmer/<int:pk>/', views.retrieve_farmer, name='retrieve_farmer'),
    path('farmer/<int:pk>/update/', views.update_farmer, name='update_farmer'),
    path('farmer/<int:pk>/delete/', views.delete_farmer, name='delete_farmer'),
    path('rancher/create/', views.create_rancher, name='create_rancher'),
    path('rancher/<int:pk>/', views.retrieve_rancher, name='retrieve_rancher'),
    path('rancher/<int:pk>/update/', views.update_rancher, name='update_rancher'),
    path('rancher/<int:pk>/delete/', views.delete_rancher, name='delete_rancher'),
    path('consumer/create/', views.create_consumer, name='create_consumer'),
    path('consumer/<int:pk>/', views.retrieve_consumer, name='retrieve_consumer'),
    path('consumer/<int:pk>/update/', views.update_consumer, name='update_consumer'),
    path('consumer/<int:pk>/delete/', views.delete_consumer, name='delete_consumer'),
]
