Funcionalidades/chat/urls.py
from django.urls import path

from . import views
from django.urls import path
from . import views

urlpatterns = [
    # Rutas de la interfaz de usuario
    path('', views.conversations, name='conversations'),
    path('<int:conversation_id>/', views.conversation, name='conversation'),
    path('<int:conversation_id>/new_message/', views.new_message, name='new_message'),

    # Rutas WebSocket
    path('ws/', views.ChatConsumer.as_asgi(), name='chat'),

    # Rutas de mensajería
    path('messages/', views.messages, name='messages'),
    path('messages/<int:message_id>/', views.message_detail, name='message_detail'),
    path('messages/<int:message_id>/reply/', views.reply_message, name='reply_message'),
]
