
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Notification

@login_required
def notifications(request):
    user = request.user
    notifications = Notification.objects.filter(user=user).order_by('-timestamp')
    context = {'notifications': notifications}
    return render(request, 'notifications.html', context)

@login_required
def generate_notification(request, event_type, message):
    user = request.user
    notification = Notification(user=user, event_type=event_type, message=message)
    notification.save()

@login_required
def manage_notifications(request):
    user = request.user
    notifications = Notification.objects.filter(user=user).order_by('-timestamp')
    context = {'notifications': notifications}
    return render(request, 'manage_notifications.html', context)


