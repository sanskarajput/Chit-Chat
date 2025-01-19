from django.db import models
from django.contrib.auth.models import User

# Creating models here.
class Conversation(models.Model):
    user1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='conversation_s_user_1')
    user2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='conversation_s_user_2')   
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user1', 'user2'], name='unique_conversation_users')  # Ensuring that only unique conversations are created between two users.
        ]

    def __str__(self):
        return f'Conversation between {self.user1.username} and {self.user2.username}'


class Message(models.Model):
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE, related_name='messages')
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='message_s_sender')
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Message from {self.sender.username} in Conversation {self.conversation.id}"
