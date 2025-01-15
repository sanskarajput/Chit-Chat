from django.shortcuts import render

# Creating views here.
def start_conversation(request):
    return render(request, 'start-conversation.html',{'title': 'Start Conversation'})

def chatting_with(request, username):
    return render(request, 'start-conversation.html',{'title': 'Chatting with username'})