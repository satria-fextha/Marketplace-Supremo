from django.urls import path
from . import views

urlpatterns = [
    # URL for sending a message
    path('send-message/', views.send_message, name='send_message'),

    # URL for viewing a message
    path('view-message/<int:message_id>/', views.view_message, name='view_message'),

    # URL for listing all messages
    path('messages/', views.list_messages, name='list_messages'),
]
