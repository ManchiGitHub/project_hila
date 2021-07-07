import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer

class ChatConsumer(WebsocketConsumer):

    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        if text_data_json is not None:
            message = text_data_json['message']
            print("consumer got message: " + message)
            self.send(text_data=json.dumps({
                'message': message
            }))

    
    

