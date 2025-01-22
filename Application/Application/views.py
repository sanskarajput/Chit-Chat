from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from chats.views import all_users, details
from django.contrib import messages


def index(request):
    return render(request, 'index.html', {'title': 'Chit Chat'})

def my_admin_login(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('/admin')

def auth(request):
    if request.user.is_authenticated:
        return redirect('start-conversation')
    form_type = request.session.pop('form_type', "Sign Up")  # Retrieve and remove it from session
    return render(request, 'auth/auth.html', {'title': form_type, 'users': all_users(), 'details': details(request.user) })

def sign_up(request):
    if request.user.is_authenticated:
        return redirect('start-conversation')
    if request.method == 'POST':
        email = request.POST['email']
        fullname = request.POST['fullname']
        username = request.POST['username']
        password = request.POST['password']
        # Check if email and username already exist
        if User.objects.filter(email=email).exists() or User.objects.filter(username=username).exists():
            messages.error(request,"Email or username already exists !")
            return redirect('auth')
        # Create user
        created_user = User.objects.create_user(username=username, email=email, password=password, first_name=fullname)
        created_user.save()
        email,fullname,username,password = "", "", "",""
        request.session['form_type'] = 'Sign In'
        messages.success(request,"Sign Up successfully !")
        return redirect('auth')
    request.session['form_type'] = 'Sign Up'
    return redirect('auth')


def log_in(request):
    if request.user.is_authenticated:
        return redirect('start-conversation')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        username, password = "", ""
        if user is not None:
            login(request, user)
            messages.success(request,"You are logged in successfully !")
            return redirect('start-conversation')
        else:
            request.session['form_type'] = 'Sign In'
            messages.error(request,"Invalid username or password!")
            return redirect('auth')
    request.session['form_type'] = 'Sign In'
    return redirect('auth')


def logout_user(request):
    logout(request)
    request.session['form_type'] = 'Sign In'
    messages.success(request,"You are logged out !")
    return redirect('auth')