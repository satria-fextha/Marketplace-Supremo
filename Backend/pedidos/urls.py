from django.urls import path
from . import views

urlpatterns = [
    # URL for sellers to manage orders
    path('orders/', views.manage_orders, name='manage_orders'),

    # URL for consumers to view order status
    path('orders/<int:order_id>/', views.view_order_status, name='view_order_status'),
]
