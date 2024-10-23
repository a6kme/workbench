# your_app_name/consumers.py
import json

from channels.generic.websocket import AsyncWebsocketConsumer


class Echo(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data['message']

        # Echo the message back to the client
        await self.send(text_data=json.dumps({
            'message': message
        }))
