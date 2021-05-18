from django.contrib import admin
from django.urls import path, include
from helpinghandhome import views

urlpatterns = [
    path('', views.index, name="index"),
    path('login', views.login, name="login"),
    path('register', views.register, name="register"),
    path('home_detail', views.home_detail, name="home_detail"),
    path('logout', views.logout_view, name="logout_view"),
    path('food_details', views.food_details, name="food_details"),
    path('user_profile', views.user_profile, name="user_profile"),
    path('supplier_dashboard', views.supplier_dashboard, name="supplier_dashboard"),
    
]
