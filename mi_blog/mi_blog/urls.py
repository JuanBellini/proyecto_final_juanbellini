"""
URL configuration for mi_blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from blog import views as blog
from accounts import views as accounts
from profiles import views as profiles
from user_messages import views as user_messages

 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', blog.views.about, name='about'),
    path('pages/', blog.views.blog_list, name='blog_list'),
    path('accounts/signup/', accounts.views.signup, name='singup'),
    path('accounts/login/', accounts.view.login, name='login'),
    path('accounts/profiles/', profiles.views.profile, name='profile'),
    path('user_messages/', user_messages.views.messages_list, name='messages_list'),


]
