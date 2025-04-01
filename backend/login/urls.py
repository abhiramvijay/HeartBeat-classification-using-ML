from . import views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('register', views.registerPage, name='register'),
    path('', views.homepage, name='Home'),
    path('login', views.loginpage, name='login'),
    path('loginerror', views.loginpage, name='loginerror'),
    path('postlogin', views.postlogin, name='postlogin'),
    path('predict', views.predict_arrhythmia, name='predict'),
]