from django import forms   
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

class LoginForm(forms.Form):
    username = forms.CharField(
        label='Username',
        widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'username'})
    )
    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'id': 'password'})
    )
    
class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password'}),
        }

class TaskForm(forms.ModelForm):
    id_task = forms.CharField(
        required=True,
        label='ID',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter task ID'
        })
    )
    n_task = forms.CharField(
        required=True,
        label='Name',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter task name'
        })
    )
    dc_task = forms.CharField(
        required=True,
        label='Description',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter task description'
        })
    )
    dr_task = forms.CharField(
        required=True,
        label='Duration',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter task duration'
        })
    )

    class Meta:
        model = Task
        fields = '__all__'  # This specifies that all fields should be used

class AddEmployeeTask(forms.ModelForm):
    id_employee=forms.CharField(required=True, label='ID')
    n_employee=forms.CharField(required=True, label='Name')


    class Meta:
        model=Employee
        fields=['id','name']
        fields='__all__'




class ModifyTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['id_task', 'n_task', 'dc_task', 'dr_task']  # Fields to include
        widgets = {
            'id_task': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter task ID',
                'readonly': 'readonly'  # Making ID readonly if it should not be changed
            }),
            'n_task': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter task name'
            }),
            'dc_task': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter task description'
            }),
            'dr_task': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter task duration'
            }),
        }