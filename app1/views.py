from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from .forms import *
# Create your views here.
def login_page(request):
    if request.method=='POST':
        form=LoginForm(request.POST) 

        if form.is_valid():
            username=form.cleaned_data['username']
            print(username)

            return HttpResponseRedirect(reverse('register'))

        else:
                return render(request,'app1\login.html',{
                'form':LoginForm()})

    return render(request,'app1\login.html',{
                'form':LoginForm()})
    


def register_page(request):
    return render(request,'app1\\register.html')