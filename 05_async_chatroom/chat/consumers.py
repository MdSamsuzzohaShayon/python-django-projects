from channels.generic.websocket import AsyncWebsocketConsumer
import json


class ChatRoomConsumer(AsyncWebsocketConsumer):
    # Connect to group https://channels.readthedocs.io/en/latest/topics/channel_layers.html#groups
    async def connect(self):
        self.room_name = self.scope["url_route", "kwargs", "room_name"]
        self.room_group_name = 'chat_%s' % self.room_name

        # create a group and that group will be utilizing this class
        # Add confluence to the group - need two thing, room group name, channel name
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        # Send a message to group https://channels.readthedocs.io/en/latest/topics/channel_layers.html#what-to-send-over-the-channel-layer
        await self.channel_layer.group_send(
            self.room_group_name,
            {"typer": "tester_message", "tester": "tester"}
        )

    # Discard the group - https://channels.readthedocs.io/en/latest/topics/channel_layers.html#groups
    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )
