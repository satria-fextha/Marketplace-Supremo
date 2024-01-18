from django.urls import path
from . import views

app_name = 'recomendaciones'

urlpatterns = [
    path('recomendar/', views.recommend_products, name='recommend_products'),
]
