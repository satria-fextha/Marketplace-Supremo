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

# Messaging functionality
from notifications.consumers import MessageConsumer

application = ProtocolTypeRouter({
    "websocket": URLRouter([
        path("chat/", ChatConsumer.as_asgi()),
        path("message/", MessageConsumer.as_asgi()),
    ])
})
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
