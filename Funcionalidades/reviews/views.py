Funcionalidades/reviews/views.py
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Producto, Vendedor, Calificacion, Resena
from .forms import CalificacionForm, ResenaForm

@login_required
def calificar_producto(request, producto_id):
    producto = get_object_or_404(Producto, pk=producto_id)
    if request.method == 'POST':
        form = CalificacionForm(request.POST)
        if form.is_valid():
            calificacion = form.save(commit=False)
            calificacion.producto = producto
            calificacion.usuario = request.user
            calificacion.save()
            messages.success(request, '¡Gracias por calificar este producto!')
            return HttpResponseRedirect(reverse('detalle_producto', args=[producto.id]))
    else:
        form = CalificacionForm()
    return render(request, 'calificar_producto.html', {'producto': producto, 'form': form})

@login_required
def calificar_vendedor(request, vendedor_id):
    vendedor = get_object_or_404(Vendedor, pk=vendedor_id)
    if request.method == 'POST':
        form = CalificacionForm(request.POST)
        if form.is_valid():
            calificacion = form.save(commit=False)
            calificacion.vendedor = vendedor
            calificacion.usuario = request.user
            calificacion.save()
            messages.success(request, '¡Gracias por calificar a este vendedor!')
            return HttpResponseRedirect(reverse('detalle_vendedor', args=[vendedor.id]))
    else:
        form = CalificacionForm()
    return render(request, 'calificar_vendedor.html', {'vendedor': vendedor, 'form': form})

@login_required
def escribir_resena(request, producto_id):
    producto = get_object_or_404(Producto, pk=producto_id)
    if request.method == 'POST':
        form = ResenaForm(request.POST)
        if form.is_valid():
            resena = form.save(commit=False)
            resena.producto = producto
            resena.usuario = request.user
            resena.save()
            messages.success(request, '¡Gracias por escribir una reseña para este producto!')
            return HttpResponseRedirect(reverse('detalle_producto', args=[producto.id]))
    else:
        form = ResenaForm()
    return render(request, 'escribir_resena.html', {'producto': producto, 'form': form})

@login_required
def reportar_resena(request, resena_id):
    resena = get_object_or_404(Resena, pk=resena_id)
    if request.method == 'POST':
        resena.reportada = True
        resena.save()
        messages.success(request, '¡Gracias por reportar esta reseña! La revisaremos pronto.')
        return HttpResponseRedirect(reverse('detalle_producto', args=[resena.producto.id]))
    else:
        return render(request, 'reportar_resena.html', {'resena': resena})
