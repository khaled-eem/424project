from django import forms   


class LoginForm(forms.Form):
    username=forms.CharField(label='UserName', )
    password=forms.CharField(label='Password', )
    
