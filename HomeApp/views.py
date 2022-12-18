from django.shortcuts import render
from . import models

def HomeView(request):
   data = models.StudentRegister.objects.all()
   
   
   
   html = 'home.html'
   context = {
      'Students':data,
      }
   return render(request,html,context)



def AboutView(request):

   return render(request,'about.html',{})