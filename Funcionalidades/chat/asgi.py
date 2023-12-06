from channels.routing import ProtocolTypeRouter, URLRouter

application = ProtocolTypeRouter({
    "websocket": URLRouter([
        path("", ChatConsumer.as_asgi()),
    ])
})

from channels.asgi import run_server

run_server(application)
