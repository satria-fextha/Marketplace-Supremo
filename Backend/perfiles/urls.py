from django.urls import path
from .views import AgricultorViewSet, GanaderoViewSet, ConsumidorViewSet

urlpatterns = [
    path('agricultores/', AgricultorViewSet.as_view({'get': 'list', 'post': 'create'}), name='agricultores'),
    path('agricultores/<int:pk>/', AgricultorViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='agricultor-detail'),
    path('ganaderos/', GanaderoViewSet.as_view({'get': 'list', 'post': 'create'}), name='ganaderos'),
    path('ganaderos/<int:pk>/', GanaderoViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='ganadero-detail'),
    path('consumidores/', ConsumidorViewSet.as_view({'get': 'list', 'post': 'create'}), name='consumidores'),
    path('consumidores/<int:pk>/', ConsumidorViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='consumidor-detail'),
]
