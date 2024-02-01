from django.urls import path
from . import views

urlpatterns = [
    # URLs for Productos
    path('api/productos/', views.ProductoList.as_view(), name='producto-list'),
    path('api/productos/<int:pk>/', views.ProductoDetail.as_view(), name='producto-detail'),
    # URLs for Búsqueda y Filtros
    path('api/busqueda/', views.BusquedaList.as_view(), name='busqueda-list'),
    path('api/filtros/', views.FiltrosList.as_view(), name='filtros-list'),
]
