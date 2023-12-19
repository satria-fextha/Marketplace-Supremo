from django.urls import path
from . import views

urlpatterns = [
    path('products/<int:product_id>/rate/', views.rate_product, name='rate_product'),
    path('vendors/<int:vendor_id>/rate/', views.rate_vendor, name='rate_vendor'),
    path('reviews/report/<int:review_id>/', views.report_review, name='report_review'),
]

from . import views

urlpatterns = [
    path('', views.all_products, name='all_products'),
    path('products/<int:product_id>/', views.product_detail, name='product_detail'),
    path('reviews/submit/', views.review_submit, name='review_submit'),
]
