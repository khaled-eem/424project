from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from .models import *
from .forms import *

# Create your views here.
def login_page(request):
    if request.method=='POST':
        form=LoginForm(request.POST) 

        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user=authenticate(request,username=username,password=password)
            
            if user:
                 login(request,user)
                 return HttpResponseRedirect(reverse('main'))
            else:
                return render(request,'app1/login.html',{
                     "message":"Inavalid Password or Username",
                     'form':LoginForm()
                })

            

        else:
                return render(request,'app1\login.html',{
                'form':LoginForm()})

    return render(request,'app1\login.html',{
                'form':LoginForm()})
    
def main_page(request):
    return render(request,'app1/main.html',{
         'tasks':Task.objects.all()
    })

def register_page(request):
    return render(request,'app1\\register.html')

def logout_page(request):
     logout()
     return render(request,'app1/login.html',{
          'message':'Logged out',
          'form':LoginForm()
     })