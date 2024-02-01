from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Notification

@login_required
def notifications(request):
    user = request.user
    notifications = Notification.objects.filter(user=user).order_by('-created_at')
    return render(request, 'notifications.html', {'notifications': notifications})

# Implement your event-based notification logic here

