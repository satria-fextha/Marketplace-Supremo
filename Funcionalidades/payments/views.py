
from decimal import Decimal
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.urls import reverse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from paypal.standard.forms import PayPalPaymentsForm
from .models import Order

@login_required
def payment_process(request):
    order_id = request.session.get('order_id')
    order = Order.objects.get(id=order_id)
    host = request.get_host()
    paypal_dict = {
        'business': settings.PAYPAL_RECEIVER_EMAIL,
        'amount': '%.2f' % order.get_total_cost().quantize(Decimal('.01')),
        'item_name': 'Order {}'.format(order.id),
        'invoice': str(order.id),
        'currency_code': 'USD',
        'notify_url': 'http://{}{}'.format(host, reverse('paypal-ipn')),
        'return_url': 'http://{}{}'.format(host, reverse('payment:done')),
        'cancel_return': 'http://{}{}'.format(host, reverse('payment:canceled')),
    }
    form = PayPalPaymentsForm(initial=paypal_dict)
    return render(request, 'payment/process.html', {'order': order, 'form': form})

@csrf_exempt
def payment_done(request):
    order_id = request.session.get('order_id')
    order = Order.objects.get(id=order_id)
    order.paid = True
    order.save()
    # Generate invoice or receipt logic here
    # Send notification to the consumer
    return render(request, 'payment/done.html')

@csrf_exempt
def payment_canceled(request):
    # Handle payment cancellation logic here
    return render(request, 'payment/canceled.html')

# Additional code for integrating with other payment gateways and charging commissions
# ...

# Integration with other payment gateways
def integrate_payment_gateway(request):
    # Code for integrating with other payment gateways
    return render(request, 'payment/integrate_payment_gateway.html')

# Charging commissions for sales
def charge_commissions(request):
    # Code for charging commissions for sales
    return render(request, 'payment/charge_commissions.html')


