from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.forms.models import model_to_dict
import json

# Creating views here.
def start_conversation(request):
    if not request.user.is_authenticated:
        request.session['form_type'] = 'Sign In'
        return redirect('auth')
    users = User.objects.all().defer('password')
    return render(request, 'start-conversation.html',{'title': 'Start Conversation', 'users': users})

def chatting_with(request, username):
    if not request.user.is_authenticated:
        request.session['form_type'] = 'Sign In'
        return redirect('auth')
    try:
        user = User.objects.get(username=username)
        user = model_to_dict(user) # Serialize the user object to JSON

        users = User.objects.all() # for Sidebar to display
        return render(request, 'chatting-with.html',{'title': f'Chatting with {user['first_name']}', 'users': users, 'other_user':user})
    except User.DoesNotExist:
        return redirect('does-not-exist',username = username)
    
def does_not_exist(request,username):
    if not request.user.is_authenticated:
        request.session['form_type'] = 'Sign In'
        return redirect('auth')
    return render(request, 'does-not-exist.html', {'title': 'User Not Found'})
