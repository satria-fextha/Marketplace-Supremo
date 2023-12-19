<!-- FILEPATH:/c:/Users/jorge/OneDrive/Escritorio/Marketplace/Funcionalidades/chat/ChatConsumer.py
from channels.routing import ProtocolTypeRouter, URLRouter

application = ProtocolTypeRouter({
    "websocket": URLRouter([
        path("", ChatConsumer.as_asgi()),
    ])
})
