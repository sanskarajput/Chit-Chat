from django.contrib import admin

# Registering models here.
from .models import Conversation, Message

admin.site.register(Conversation)
admin.site.register(Message)
