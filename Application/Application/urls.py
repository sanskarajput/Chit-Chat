"""
URL configuration for Application project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin', admin.site.urls),
    path('my-admin-login', views.my_admin_login, name='my-admin-login'),
    path('auth', views.auth, name='auth'),
    path('log-in', views.log_in, name='log-in'),
    path('sign-up', views.sign_up, name='sign-up'),
    path('logout', views.logout_user, name='logout'),
    path('', include('chats.urls')), # if not authenticated -> index and if authenticated -> start-conversation
]

