from . import views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('register', views.registerPage, name='register'),
    path('', views.loginpage, name='login'),
    path('postlogin', views.postlogin, name='postlogin.html'),
]
