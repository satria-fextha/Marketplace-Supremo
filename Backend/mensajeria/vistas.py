from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from .models import Message

@login_required
def send_message(request, recipient_id):
    recipient = get_object_or_404(User, id=recipient_id)
    if request.method == 'POST':
        message_text = request.POST.get('message_text')
        message = Message(sender=request.user, recipient=recipient, text=message_text)
        message.save()
        # Lógica adicional para notificaciones o redireccionamientos se puede agregar aquí
    return render(request, 'send_message.html', {'recipient': recipient})

@login_required
def inbox(request):
    received_messages = Message.objects.filter(recipient=request.user)
    return render(request, 'inbox.html', {'received_messages': received_messages})

@login_required
def sent_messages(request):
    sent_messages = Message.objects.filter(sender=request.user)
    return render(request, 'sent_messages.html', {'sent_messages': sent_messages})
