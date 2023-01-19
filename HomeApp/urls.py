from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView, name='home'),
    path('login/', views.LoginView, name='login'),
    path('error/', views.ErrorView, name='error'),
]