from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.register, name='register'),
    path('farmer_register/', views.farmer_register, name='farmer_register'),
    path('rancher_register/', views.rancher_register, name='rancher_register'),
    path('consumer_register/', views.consumer_register, name='consumer_register'),
    path('verify_email/', views.verify_email, name='verify_email'),
    path('profile/', views.profile, name='profile'),
]
