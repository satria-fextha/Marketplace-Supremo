from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Producto, Vendedor, Calificacion, Resena

@csrf_exempt
def publicar_calificacion(request):
    if request.method == 'POST':
        producto_id = request.POST.get('producto_id')
        vendedor_id = request.POST.get('vendedor_id')
        calificacion = request.POST.get('calificacion')
        resena = request.POST.get('resena')

        producto = get_object_or_404(Producto, id=producto_id)
        vendedor = get_object_or_404(Vendedor, id=vendedor_id)

        # Crear la calificación y la reseña
        calificacion_obj = Calificacion.objects.create(producto=producto, vendedor=vendedor, calificacion=calificacion)
        Resena.objects.create(calificacion=calificacion_obj, resena=resena)

        return JsonResponse({'message': 'Calificación y reseña publicadas exitosamente.'})
    else:
        return JsonResponse({'error': 'Método no permitido.'}, status=405)

@csrf_exempt
def moderar_resenas(request):
    if request.method == 'GET':
        resenas_pendientes = Resena.objects.filter(aprobada=False)

        # Lógica para revisar y aprobar las reseñas pendientes

        return JsonResponse({'message': 'Reseñas moderadas exitosamente.'})
    else:
        return JsonResponse({'error': 'Método no permitido.'}, status=405)
