from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import Family
from django.contrib.auth.models import User

class login_1(forms.Form):
    Username = forms.CharField(label='username',max_length=30)
    Password = forms.CharField(label='password',max_length=30,widget=forms.PasswordInput)

class CreateUserForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']