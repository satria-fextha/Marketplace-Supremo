from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import Producto, Carro

def agregar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    carro, created = Carro.objects.get_or_create(usuario=request.user)
    carro.agregar_producto(producto)
    return JsonResponse({'mensaje': 'Producto agregado al carro correctamente'})

def actualizar_cantidad(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    carro = get_object_or_404(Carro, usuario=request.user)
    cantidad = request.POST.get('cantidad')
    carro.actualizar_cantidad(producto, cantidad)
    return JsonResponse({'mensaje': 'Cantidad actualizada correctamente'})

def eliminar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    carro = get_object_or_404(Carro, usuario=request.user)
    carro.eliminar_producto(producto)
    return JsonResponse({'mensaje': 'Producto eliminado del carro correctamente'})
