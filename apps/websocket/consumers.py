import json
from channels.generic.websocket import AsyncWebsocketConsumer


class CategoryStageConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.category = self.scope["url_route"]["kwargs"]["category"]
        self.stage = self.scope["url_route"]["kwargs"]["stage"]
        self.group_name = f"category_{self.category}_stage_{self.stage}"

        # Join group
        await self.channel_layer.group_add(self.group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        # Leave group
        await self.channel_layer.group_discard(self.group_name, self.channel_name)

    async def receive(self, text_data):
        pass  # Placeholder for receiving messages (if needed)

    async def send_update(self, event):
        await self.send(text_data=json.dumps(event["data"]))
