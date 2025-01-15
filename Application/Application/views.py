from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html', {'title': 'Hello, world!'})
    # return HttpResponse("Hello, world. You're at the polls index.")
