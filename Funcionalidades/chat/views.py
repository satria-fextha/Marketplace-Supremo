Funcionalidades/chat/views.py
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone

from .models import Message, Conversation

@login_required
def conversations(request):
    conversations = Conversation.objects.filter(users=request.user)
    return render(request, 'chat/conversations.html', {'conversations': conversations})

@login_required
def conversation(request, conversation_id):
    conversation = get_object_or_404(Conversation, id=conversation_id, users=request.user)
    messages = conversation.messages.all().order_by('created_at')
    return render(request, 'chat/conversation.html', {'conversation': conversation, 'messages': messages})

@login_required
def new_message(request, conversation_id):
    conversation = get_object_or_404(Conversation, id=conversation_id, users=request.user)
    if request.method == 'POST':
        message = Message.objects.create(
            conversation=conversation,
            sender=request.user,
            text=request.POST.get('text'),
            created_at=timezone.now()
        )
        message.save()
        messages.success(request, 'Mensaje enviado exitosamente.')
        # Send notification to both consumer and seller
        # Code for sending notification goes here
        return HttpResponseRedirect(reverse('chat:conversation', args=[conversation.id]))
    else:
        return render(request, 'chat/new_message.html', {'conversation': conversation})
