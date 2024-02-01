from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from .models import Producto

@csrf_exempt
@login_required
def crear_producto(request):
    if request.method == 'POST':
        # Obtener los datos del producto del cuerpo de la solicitud
        nombre = request.POST.get('nombre')
        categoria = request.POST.get('categoria')
        precio = request.POST.get('precio')
        # Crear el nuevo producto en la base de datos
        producto = Producto(nombre=nombre, categoria=categoria, precio=precio)
        producto.save()
        return JsonResponse({'mensaje': 'Producto creado exitosamente'})
    else:
        return JsonResponse({'error': 'Método no permitido'})

@login_required
def obtener_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    # Retornar los datos del producto en formato JSON
    return JsonResponse({'nombre': producto.nombre, 'categoria': producto.categoria, 'precio': producto.precio})

@csrf_exempt
@login_required
def actualizar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    if request.method == 'POST':
        # Obtener los datos actualizados del producto del cuerpo de la solicitud
        nombre = request.POST.get('nombre')
        categoria = request.POST.get('categoria')
        precio = request.POST.get('precio')
        # Actualizar los atributos del producto en la base de datos
        producto.nombre = nombre
        producto.categoria = categoria
        producto.precio = precio
        producto.save()
        return JsonResponse({'mensaje': 'Producto actualizado exitosamente'})
    else:
        return JsonResponse({'error': 'Método no permitido'})

@login_required
def eliminar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    # Eliminar el producto de la base de datos
    producto.delete()
    return JsonResponse({'mensaje': 'Producto eliminado exitosamente'})
