
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Notification

@login_required
def notifications(request):
    user = request.user
    notifications = Notification.objects.filter(user=user).order_by('-timestamp')
    context = {'notifications': notifications}
    return render(request, 'notifications.html', context)

