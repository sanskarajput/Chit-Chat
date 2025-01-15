from django.urls import path
from . import views

# configuring views here.
urlpatterns = [
    # path('', views.index, name='index'),  # index page if not authenticated
    path('start-conversation', views.start_conversation, name='start-conversation'),
    path('chatting-with-<str:username>', views.chatting_with, name='chatting-with-user')
]
