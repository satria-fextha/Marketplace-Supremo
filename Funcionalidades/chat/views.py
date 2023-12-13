
Explicación:

Este archivo de Python define tres vistas de Django para administrar la interfaz de usuario de una aplicación de chat.

Conversaciones de Vista:

Esta vista de Django se utiliza para mostrar una lista de conversaciones a las que el usuario actual está suscrito. La vista filtra las conversaciones en función de la propiedad users de la clase Conversation y recupera solo las conversaciones que contienen al usuario actual. Luego, renderiza la plantilla chat/conversations.html y pasa una lista de conversaciones a la plantilla.

Conversación de vista:

Esta vista de Django se utiliza para mostrar una conversación específica. La vista recibe un ID de conversación como parámetro y recupera la conversación correspondiente de la base de datos. Luego, recupera todos los mensajes de la conversación y los ordena por la fecha de creación. Finalmente, renderiza la plantilla chat/conversation.html y pasa la conversación y la lista de mensajes a la plantilla.

Vista nuevo_mensaje:

Esta vista de Django se utiliza para crear nuevos mensajes en una conversación. La vista recibe un ID de conversación como parámetro y recupera la conversación correspondiente de la base de datos. Si el método de solicitud es POST, la vista recibe el texto del mensaje y crea un nuevo objeto de mensaje en la base de datos. El mensaje se guarda y se envía una confirmación al usuario. Luego, redirige al usuario a la vista conversation para la conversación actual. De lo contrario, renderiza la plantilla chat/new_message.html y pasa la conversación a la plantilla.

Uso:

Estas vistas se utilizan para proporcionar la interfaz de usuario para una aplicación de chat básica. La vista conversations muestra una lista de conversaciones, la vista conversation muestra una conversación específica, y la vista new_message permite a los usuarios enviar nuevos mensajes.

Rutas:

Las vistas de Django se asocian a las siguientes rutas:

/chat/conversations/: Esta ruta se asocia a la vista conversations.
/chat/conversations/<int:conversation_id>/: Esta ruta se asocia a la vista conversation.
/chat/conversations/<int:conversation_id>/new_message/: Esta ruta se asocia a la vista new_message.
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
        return HttpResponseRedirect(reverse('chat:conversation', args=[conversation.id]))
    else:
        return render(request, 'chat/new_message.html', {'conversation': conversation})
