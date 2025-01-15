from django.http import HttpResponse
from django.shortcuts import render, redirect


def index(request):
    return render(request, 'index.html', {'title': 'Hello, world!'})
    # return HttpResponse("Hello, world. You're at the polls index.")


def sign_up(request):
    if request.user.is_authenticated:
        return redirect('start-conversation')
    return render(request, 'auth/sign-up.html', {'title': 'Sign Up'})


def log_in(request):
    if request.user.is_authenticated:
        return redirect('start-conversation')
    return render(request, 'auth/log-in.html', {'title': 'Log In'})