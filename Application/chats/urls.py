from django.urls import path, reverse_lazy
from django.views.generic.base import RedirectView
from . import views

# configuring views here.
urlpatterns = [
    path('', RedirectView.as_view(url=reverse_lazy('start-conversation')), name='chat-room-index'), # index page if not authenticated
    path('start-conversation', views.start_conversation, name='start-conversation'),
    path('chatting-with-<str:username>', views.chatting_with, name='chatting-with-user'),
    path('<str:username>-does-not-exist', views.does_not_exist, name='does-not-exist')
]
