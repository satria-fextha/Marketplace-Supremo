<!-- FILEPATH:/c:/Users/jorge/OneDrive/Escritorio/Marketplace/Funcionalidades/chat/ChatConsumer.py
from channels.generic.websocket import AsyncWebsocketConsumer
import json

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Code for connecting to the websocket
        
        # Add the consumer to a group based on their role (consumer or vendor)
        if self.scope["user"].is_authenticated:
            if self.scope["user"].is_consumer:
                await self.channel_layer.group_add("consumers", self.channel_name)
            elif self.scope["user"].is_vendor:
                await self.channel_layer.group_add("vendors", self.channel_name)
        
        await self.accept()

    async def disconnect(self, close_code):
        # Code for disconnecting from the websocket
        
        # Remove the consumer from the group
        if self.scope["user"].is_authenticated:
            if self.scope["user"].is_consumer:
                await self.channel_layer.group_discard("consumers", self.channel_name)
            elif self.scope["user"].is_vendor:
                await self.channel_layer.group_discard("vendors", self.channel_name)

    async def receive(self, text_data):
        # Code for receiving and processing messages
        
        # Send the message to the appropriate group (consumers or vendors)
        if self.scope["user"].is_authenticated:
            if self.scope["user"].is_consumer:
                await self.channel_layer.group_send(
                    "vendors",
                    {
                        "type": "chat_message",
                        "message": text_data
                    }
                )
            elif self.scope["user"].is_vendor:
                await self.channel_layer.group_send(
                    "consumers",
                    {
                        "type": "chat_message",
                        "message": text_data
                    }
                )

    async def chat_message(self, event):
        # Code for sending messages to the websocket
        
        # Send the message to the consumer or vendor
        message = event["message"]
        await self.send(text_data=json.dumps({
            "message": message
        }))
from channels.routing import ProtocolTypeRouter, URLRouter

application = ProtocolTypeRouter({
    "websocket": URLRouter([
        path("", ChatConsumer.as_asgi()),
    ])
})
