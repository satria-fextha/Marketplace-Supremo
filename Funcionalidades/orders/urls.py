from django.urls import path

from . import views

urlpatterns = [
    path('', views.order_list, name='order_list'),
    path('order/<int:order_id>/', views.order_detail, name='order_detail'),
    path('order/update/<int:order_id>/', views.update_order, name='update_order'),
    path('cart/', views.cart, name='cart'),
    path('order/manage/', views.manage_orders, name='manage_orders'),
    path('order/manage/accept/<int:order_id>/', views.accept_order, name='accept_order'),
    path('order/manage/reject/<int:order_id>/', views.reject_order, name='reject_order'),
    path('order/manage/update/<int:order_id>/', views.update_order_status, name='update_order_status'),
    path('checkout/', views.checkout, name='checkout'),
]
