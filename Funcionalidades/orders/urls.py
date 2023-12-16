from django.urls import path

from . import views

urlpatterns = [
    path('', views.order_list, name='order_list'),
    path('order/<int:order_id>/', views.order_detail, name='order_detail'),
    path('order/update/<int:order_id>/', views.update_order, name='update_order'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
]
