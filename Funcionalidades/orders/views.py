
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Order, OrderItem
from .forms import AddToCartForm

@login_required
def order_list(request):
    orders = Order.objects.all()
    context = {'orders': orders}
    return render(request, 'order_list.html', context)

@login_required
def order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    context = {'order': order}
    return render(request, 'order_detail.html', context)

@login_required
def accept_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    order.status = 'accepted'
    order.save()
    messages.success(request, f"El pedido {order.id} ha sido aceptado.")
    return redirect('order_detail', order_id=order.id)

@login_required
def reject_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    order.status = 'rejected'
    order.save()
    messages.success(request, f"El pedido {order.id} ha sido rechazado.")
    return redirect('order_detail', order_id=order.id)

@login_required
def update_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    form = AddToCartForm(request.POST or None, instance=order)
    if form.is_valid():
        form.save()
        messages.success(request, f"El pedido {order.id} ha sido actualizado.")
    return redirect('order_detail', order_id=order.id)

@login_required
def order_status(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    context = {'order': order}
    return render(request, 'order_status.html', context)
