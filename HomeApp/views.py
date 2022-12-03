from django.shortcuts import render

def HomeView(request):
   
   return render(request,'home.html',{})



def AboutView(request):

   return render(request,'about.html',{})