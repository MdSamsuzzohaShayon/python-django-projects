# This is not stateless
from channels.generic.websocket import WebsocketConsumer
from channels.generic.websocket import AsyncJsonWebsocketConsumer
from asgiref.sync import async_to_sync
import json


class TestConsumer(WebsocketConsumer):

    # ws://
    # Send data backend to frontend
    def connect(self):
        # Called on connection.
        # To accept the connection call:
        # Or accept the connection and specify a chosen subprotocol.
        # A list of subprotocols specified by the connecting client
        # will be available in self.scope['subprotocols']
        # To reject the connection, call:
        self.room_name = "test_consumer_room"
        self.room_group_name = "test_consumer_group"
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        self.accept()
        self.send(text_data=json.dumps({'status': 'Conntected'}))

    # Receive data frontend to backend
    def receive(self, text_data):
        # Called with either text_data or bytes_data for each frame
        # You can call:
        # Or, to send a binary frame:
        # Want to force-close the connection? Call:
        # Or add a custom WebSocket error code!
        # print(text_data)
        # send to frontend once again
        self.send(text_data=json.dumps({"status": "Got data"}))

    def disconnect(self, close_code):
        # Called when the socket closes
        print("Disconnected")


    def send_notification(self, event):
        # print('send notification')
        # print(event)
        # print('send notification')
        data = json.loads(event.get('value'))
        self.send(text_data=json.dumps({'payload': data}))


class NewConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        self.room_name = "new_consumer"
        self.room_group_name = "new_consumer_group"

        await (self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()
        await self.send(text_data=json.dumps({"status": "connected to new async json consumer"}))

    async def receive(self, text_data):
        await self.send(text_data=json.dumps({"status": "Got data"}))

    async def disconnect(self, code):
        await print('Disconnected')


    async def send_notification(self, event):
        data = json.loads(event.get('value'))
        await self.send(text_data=json.dumps({"payload": data}))