Funcionalidades/Products/urls.py
from django.urls import path
from .views import product_detail
from .views import product_list

urlpatterns = [
    path('producto/<int:product_id>/', product_detail, name='product_detail'),

from . import views

urlpatterns = [
    path('', views.all_products, name='all_products'),
    path('categoria/<int:category_id>/', views.products_by_category, name='products_by_category'),
    path('buscar/', views.search_products, name='search_products'),
    path('filtrar/', views.filter_products, name='filter_products'),
]

