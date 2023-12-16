from django.urls import path

from . import views

urlpatterns = [
    path('', views.all_products, name='all_products'),
    path('categoria/<int:category_id>/', views.products_by_category, name='products_by_category'),
    path('buscar/', views.search_products, name='search_products'),
    path('filtrar/', views.filter_products, name='filter_products'),
]

