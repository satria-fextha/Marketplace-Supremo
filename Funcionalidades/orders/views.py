
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
    # Notify the consumer about the order status change
    # You can implement the notification logic here
    return redirect('order_detail', order_id=order.id)

@login_required
def reject_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    order.status = 'rejected'
    order.save()
    messages.success(request, f"El pedido {order.id} ha sido rechazado.")
    # Notify the consumer about the order status change
    # You can implement the notification logic here
    return redirect('order_detail', order_id=order.id)

@login_required
def update_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    form = AddToCartForm(request.POST or None, instance=order)
    if form.is_valid():
        form.save()
        messages.success(request, f"El pedido {order.id} ha sido actualizado.")
        # Notify the consumer about the order status change
        # You can implement the notification logic here
    return redirect('order_detail', order_id=order.id)

@login_required
def order_status(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    context = {'order': order}
    return render(request, 'order_status.html', context)

@login_required
def add_to_cart(request, product_id):
    # Logic to add the product to the cart
    return redirect('cart_summary')

@login_required
def cart_summary(request):
    # Logic to calculate the total and display the cart summary
    return render(request, 'cart_summary.html')

@login_required
def manage_orders(request):
    orders = Order.objects.all()
    context = {'orders': orders}
    return render(request, 'manage_orders.html', context)

@login_required
def change_order_status(request, order_id, new_status):
    order = get_object_or_404(Order, id=order_id)
    order.status = new_status
    order.save()
    messages.success(request, f"El pedido {order.id} ha sido actualizado.")
    # Notify the consumer about the order status change
    # You can implement the notification logic here
    return redirect('manage_orders')

@login_required
def view_order_status(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    context = {'order': order}
    return render(request, 'view_order_status.html', context)
