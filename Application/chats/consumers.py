import json, time
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from django.contrib.auth.models import User
from .models import Conversation, Message

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.my_id = self.scope['url_route']['kwargs']['my_id']
        self.other_id = self.scope['url_route']['kwargs']['other_id']

        created = False
        try:
            # Fetch the users
            user1 = User.objects.get(id=self.my_id)
            user2 = User.objects.get(id=self.other_id)
            other_user = user2

            # Ensure the user IDs are always in a consistent order
            if user1.id > user2.id:
                user1, user2 = user2, user1

            # Check if a conversation already exists
            self.conversation, created = Conversation.objects.get_or_create(
                user1=user1,
                user2=user2
            )

            # if created:
            #     print(f"New conversation created between {user1.username} and {user2.username}")

        except User.DoesNotExist:
            # Close the WebSocket if any user does not exist
            self.close()
            return

        # Use conversation ID for group name
        self.room_group_name = f"conversation_{self.conversation.id}"

        # Add the user to the WebSocket group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()
        if created:
            self.send(text_data=json.dumps({
                'type': 'conversation_created',
                'message': f'You have created a new conversation with {other_user.username}'
            }))
            time.sleep(.5)
        self.send(text_data=json.dumps({
            'type': 'join_group',
            'message': f'You have joined the conversation with {other_user.username}'
        }))
        time.sleep(.5)
        self.send_previous_messages()


    def disconnect(self, close_code):
        # Remove the user from the WebSocket group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    def receive(self, text_data):
        data = json.loads(text_data)
        message_content = data.get('message')
        sender_id = data.get('sender_id')

        try:
            # Validate if the sender is part of the conversation
            sender = User.objects.get(id=sender_id)
            if sender not in [self.conversation.user1, self.conversation.user2]:
                return  # Ignore messages from unauthorized users

            # Save the message to the database
            message = Message.objects.create(
                conversation=self.conversation,
                sender=sender,
                content=message_content
            )

            # Broadcast the message to the group
            async_to_sync(self.channel_layer.group_send)(
                self.room_group_name,
                {
                    'type': 'chat_message',
                    'message': {
                        'sender': sender.id,
                        'content': message.content,
                        'timestamp': message.timestamp.isoformat(),
                    }
                }
            )
        except User.DoesNotExist:
            pass  # Ignore invalid sender

    def chat_message(self, event):
        # Send the message to the WebSocket
        self.send(text_data=json.dumps({
            'message': event['message']
        }))

    def send_previous_messages(self):
        # Fetch the previous messages and send them to the WebSocket
        messages = Message.objects.filter(conversation=self.conversation).order_by('timestamp')
        for message in messages:
            self.send(text_data=json.dumps({
                'type': 'previous_messages',
                'message': {
                    'sender': message.sender.id,
                    'content': message.content,
                    'timestamp': message.timestamp.isoformat(),
                }
            }))


