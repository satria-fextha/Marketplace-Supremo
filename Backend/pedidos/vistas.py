from django.shortcuts import render, get_object_or_404
from .models import Order

def order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    context = {
        'order': order
    }
    return render(request, 'order_detail.html', context)

def confirm_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    order.status = 'Confirmed'
    order.save()
    return render(request, 'order_confirmation.html')

def prepare_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    order.status = 'Preparing'
    order.save()
    return render(request, 'order_preparation.html')

def ship_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    order.status = 'Shipped'
    order.save()
    return render(request, 'order_shipment.html')
