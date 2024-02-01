from django.shortcuts import render
from django.http import JsonResponse

from .models import Agricultor, Ganadero, Consumidor

# Crear un agricultor
def crear_agricultor(request):
    if request.method == 'POST':
        # Obtener los datos del formulario
        nombre = request.POST.get('nombre')
        edad = request.POST.get('edad')
        direccion = request.POST.get('direccion')
        # Crear el objeto Agricultor
        agricultor = Agricultor(nombre=nombre, edad=edad, direccion=direccion)
        agricultor.save()
        return JsonResponse({'message': 'Agricultor creado exitosamente'})
    else:
        return JsonResponse({'message': 'Método no permitido'})

# Leer un agricultor
def leer_agricultor(request, agricultor_id):
    try:
        agricultor = Agricultor.objects.get(id=agricultor_id)
        return JsonResponse({'nombre': agricultor.nombre, 'edad': agricultor.edad, 'direccion': agricultor.direccion})
    except Agricultor.DoesNotExist:
        return JsonResponse({'message': 'Agricultor no encontrado'})

# Actualizar un agricultor
def actualizar_agricultor(request, agricultor_id):
    if request.method == 'POST':
        try:
            agricultor = Agricultor.objects.get(id=agricultor_id)
            # Obtener los datos del formulario
            nombre = request.POST.get('nombre')
            edad = request.POST.get('edad')
            direccion = request.POST.get('direccion')
            # Actualizar los atributos del agricultor
            agricultor.nombre = nombre
            agricultor.edad = edad
            agricultor.direccion = direccion
            agricultor.save()
            return JsonResponse({'message': 'Agricultor actualizado exitosamente'})
        except Agricultor.DoesNotExist:
            return JsonResponse({'message': 'Agricultor no encontrado'})
    else:
        return JsonResponse({'message': 'Método no permitido'})

# Eliminar un agricultor
def eliminar_agricultor(request, agricultor_id):
    if request.method == 'POST':
        try:
            agricultor = Agricultor.objects.get(id=agricultor_id)
            agricultor.delete()
            return JsonResponse({'message': 'Agricultor eliminado exitosamente'})
        except Agricultor.DoesNotExist:
            return JsonResponse({'message': 'Agricultor no encontrado'})
    else:
        return JsonResponse({'message': 'Método no permitido'})
