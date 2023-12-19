"""
ASGI config for chat application.

It exposes the ASGI callable as a module-level variable named `application`.
"""

from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path

from chat.consumers import ChatConsumer

application = ProtocolTypeRouter({
    "websocket": URLRouter([
        path("", ChatConsumer.as_asgi()),
    ])
})
