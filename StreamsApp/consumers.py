import json
from channels.db import database_sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer
from django.core import serializers
from django.contrib.auth.models import User
from django.core import serializers
from django.urls import reverse
from asgiref.sync import async_to_sync

class PartyConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        self.room_name = f"room_{self.scope['url_route']['kwargs']['stream_id']}"
        await self.channel_layer.group_add(self.room_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.room_name, self.channel_name)

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        mode = text_data_json

        event = {
            'type': 'send_action',
            'mode': mode,
        }

        await self.channel_layer.group_send(self.room_name, event)

    async def send_action(self, event):

        mode = event['mode']['mode']
        user = event['mode']['user']
        
        response = {
            'mode': mode,
            'user': user
        }

        try:
            response['time'] = event['mode']['current_time']
        except KeyError:
            pass
        
        await self.send(text_data=json.dumps(response))

    