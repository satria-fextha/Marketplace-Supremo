Funcionalidades/chat/ChatConsumer.py
from channels.generic.websocket import WebsocketConsumer
from channels.generic.websocket import WebsocketConsumer
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

class ChatConsumer(WebsocketConsumer):

    def connect(self):
        self.accept()

    def receive(self, text_data):
        self.send(text_data=text_data)

    def disconnect(self):
        pass

        class ChatConsumer(WebsocketConsumer):
            def connect(self):
                self.room_name = self.scope['url_route']['kwargs']['room_name']
                self.room_group_name = 'chat_%s' % self.room_name

                # Join room group
                async_to_sync(self.channel_layer.group_add)(
                    self.room_group_name,
                    self.channel_name
                )

                self.accept()

            def disconnect(self, close_code):
                # Leave room group
                async_to_sync(self.channel_layer.group_discard)(
                    self.room_group_name,
                    self.channel_name
                )

            def receive(self, text_data):
                # Send message to room group
                async_to_sync(self.channel_layer.group_send)(
                    self.room_group_name,
                    {
                        'type': 'chat_message',
                        'message': text_data
                    }
                )

            def chat_message(self, event):
                # Send message to WebSocket
                self.send(text_data=event['message'])

