from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.forms.models import model_to_dict
from .models import Conversation, Message
from django.db.models import Q
from django.contrib import messages




def details(current_user):
    recent_users = (
        Message.objects.filter(
            Q(conversation__user1=current_user.id) | Q(conversation__user2=current_user.id)
        )
        .exclude(conversation__user1=current_user.id, conversation__user2=current_user.id)  
        .order_by('-timestamp')  # Sort by timestamp descending to get the most recent messages
        .values('conversation__user1','conversation__user2')  # Only get the required fields, we want distinct senders
        .distinct()  # Get distinct users who sent messages to the current user
    )[:3]

    # Get the actual user objects from the sender IDs
    recent_users = User.objects.filter(id__in=[user['conversation__user1'] if user['conversation__user1'] != current_user.id else user['conversation__user2'] for user in recent_users])
    total_users = User.objects.count()
    your_conversations = Conversation.objects.filter(Q(user1=current_user.id) | Q(user2=current_user.id)).count()
    details = {
                'total_users' : total_users,
                'your_conversations' : your_conversations,
                'recentUsers' : [
                    model_to_dict(user) for user in recent_users
                ]}
    return details


def all_users():
    users = User.objects.all()
    return users



# Creating views here.
def start_conversation(request):
    if not request.user.is_authenticated:
        request.session['form_type'] = 'Sign In'
        return redirect('auth')
    users = User.objects.all().defer('password')
    messages.success(request,"Start Chatting with your friends !")
    return render(request, 'start-conversation.html',{'title': 'Start Conversation', 'users': users, 'details': details(request.user)})

def chatting_with(request, username):
    if not request.user.is_authenticated:
        request.session['form_type'] = 'Sign In'
        return redirect('auth')
    try:
        user = User.objects.get(username=username)
        user = model_to_dict(user) # Serialize the user object to JSON

        messages.success(request,f"Chatting with {user['first_name']}")
        return render(request, 'chatting-with.html',{'title': f"Chatting with {user['first_name']}", 'users': all_users(), 'other_user':user, 'details': details(request.user)})
    except User.DoesNotExist:
        return redirect('does-not-exist',username = username)
    
def does_not_exist(request,username):
    if not request.user.is_authenticated:
        request.session['form_type'] = 'Sign In'
        return redirect('auth')
    messages.error(request,f"User '{username}' does not exist!")
    return render(request, 'does-not-exist.html', {'title': 'User Not Found', 'users': all_users(), 'details': details(request.user)})
