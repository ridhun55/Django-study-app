from django.shortcuts import render
from . import models

def HomeView(request):
   data = models.StudentRegister.objects.all()
   
   
   
   html = 'index.html'
   context = {
      'Students':data,
      }
   return render(request,html,context)

# ====================== LOGIN / LOGOUT ===================

from django.contrib.auth import authenticate,login,logout
from datetime import datetime, timedelta, time
from django.contrib.auth.models import User
from django.shortcuts import render,redirect


def LoginView(request):
   if request.method == 'POST':
        x = request.POST.get('username1')
        y = request.POST.get('password1')
        aut = authenticate(username = x, password = y)
        if aut is None:       
            return redirect('error')
        else:
            login(request,aut)
            if aut.is_staff:
                return redirect('home')
            else:
                return redirect('error')
             
   return render(request,'login.html',{})

def ErrorView(request):
   return render(request,'error.html',{})