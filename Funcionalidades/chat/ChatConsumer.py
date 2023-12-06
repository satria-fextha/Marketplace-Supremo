from channels.routing import ProtocolTypeRouter, URLRouter

application = ProtocolTypeRouter({
    "websocket": URLRouter([
        path("", ChatConsumer.as_asgi()),
    ])
})
