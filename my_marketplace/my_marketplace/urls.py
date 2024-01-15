from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("users/", include("users.urls")),
    path("payment/", include("payment.urls")),
    path("reviews/", include("reviews.urls")),
    path("chat/", include("chat.urls")),
    path("notifications/", include("notifications.urls")),
    path("orders/", include("orders.urls")),
    path("products/", include("products.urls")),
    path("recomendaciones/", include("recomendaciones.urls")),
]
