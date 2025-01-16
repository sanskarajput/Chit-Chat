import json
from channels.generic.websocket import WebsocketConsumer

class MyConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = 'my_consumer'
        print("Client connected!")
        self.accept()
        self.send(text_data=json.dumps({
            'message': 'GeeksforGeeks'
        }))
        pass
    
    def disconnect(self, code):
        print("Client disconnected!")
        pass
    
    def receive(self, text_data=None, bytes_data=None):
        print(f"Received message: {text_data}")
        pass