from django.contrib import admin
from django.urls import path, include
from helpinghandmain import views

urlpatterns = [
    path('', views.index, name="index"),
    path('login', views.login, name="login"),
    path('register', views.register, name="register"),
    path('home_detail', views.home_detail, name="home_detail"),
    path('logout', views.logout_view, name="logout_view"),
    
]
