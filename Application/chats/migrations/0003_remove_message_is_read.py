# Generated by Django 5.1.5 on 2025-01-19 05:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chats', '0002_conversation_unique_conversation_users'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='is_read',
        ),
    ]
