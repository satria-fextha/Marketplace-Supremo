from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Agricultor, Ganadero, Consumidor
from .serializers import AgricultorSerializer, GanaderoSerializer, ConsumidorSerializer

@api_view(['GET'])
def obtener_perfil_agricultor(request, id):
    agricultor = get_object_or_404(Agricultor, id=id)
    serializer = AgricultorSerializer(agricultor)
    return Response(serializer.data)

@api_view(['GET'])
def obtener_perfil_ganadero(request, id):
    ganadero = get_object_or_404(Ganadero, id=id)
    serializer = GanaderoSerializer(ganadero)
    return Response(serializer.data)

@api_view(['GET'])
def obtener_perfil_consumidor(request, id):
    consumidor = get_object_or_404(Consumidor, id=id)
    serializer = ConsumidorSerializer(consumidor)
    return Response(serializer.data)

@api_view(['POST'])
def crear_perfil_agricultor(request):
    serializer = AgricultorSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=201)
    return JsonResponse(serializer.errors, status=400)

@api_view(['POST'])
def crear_perfil_ganadero(request):
    serializer = GanaderoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=201)
    return JsonResponse(serializer.errors, status=400)

@api_view(['POST'])
def crear_perfil_consumidor(request):
    serializer = ConsumidorSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=201)
    return JsonResponse(serializer.errors, status=400)

@api_view(['PUT'])
def actualizar_perfil_agricultor(request, id):
    agricultor = get_object_or_404(Agricultor, id=id)
    serializer = AgricultorSerializer(agricultor, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data)
    return JsonResponse(serializer.errors, status=400)

@api_view(['PUT'])
def actualizar_perfil_ganadero(request, id):
    ganadero = get_object_or_404(Ganadero, id=id)
    serializer = GanaderoSerializer(ganadero, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data)
    return JsonResponse(serializer.errors, status=400)

@api_view(['PUT'])
def actualizar_perfil_consumidor(request, id):
    consumidor = get_object_or_404(Consumidor, id=id)
    serializer = ConsumidorSerializer(consumidor, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data)
    return JsonResponse(serializer.errors, status=400)

@api_view(['DELETE'])
def eliminar_perfil_agricultor(request, id):
    agricultor = get_object_or_404(Agricultor, id=id)
    agricultor.delete()
    return Response(status=204)

@api_view(['DELETE'])
def eliminar_perfil_ganadero(request, id):
    ganadero = get_object_or_404(Ganadero, id=id)
    ganadero.delete()
    return Response(status=204)

@api_view(['DELETE'])
def eliminar_perfil_consumidor(request, id):
    consumidor = get_object_or_404(Consumidor, id=id)
    consumidor.delete()
    return Response(status=204)
