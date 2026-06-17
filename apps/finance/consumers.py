import json
from channels.generic.websocket import AsyncWebsocketConsumer

class BalanceConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        print("Join Group")

        await self.channel_layer.group_add(
            "balance_room", 
            self.channel_name
            )
        print("channel:", self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        print("Leave Group")

        await self.channel_layer.group_discard(
            "balance_room", 
            self.channel_name
            )

    async def balance_update(self, event):
        print("event masuk")
        print(event)
        
        await self.send(
            text_data=json.dumps({
            'balances': event['balances']
            })
        )