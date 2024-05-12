from django import forms   
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

class LoginForm(forms.Form):
    username=forms.CharField(label='UserName', )
    password=forms.CharField(label='Password', )
    
class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)  # Adding email field to the form
   
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

class TaskForm(forms.ModelForm):
    id_task=forms.CharField(required=True,label='ID')
    n_task=forms.CharField(required=True,label='Name')
    dc_task=forms.CharField(required=True,label='Description')
    dr_task=forms.CharField(required=True,label='Duration')
  

    class Meta:
        model=Task        
        fields=['ID','Name','Description','Duration']
        fields='__all__'