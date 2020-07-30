from django import forms
from django.forms import ModelForm
from .models import Details_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class Details_form(ModelForm):
    class Meta:
        model = Details_model
        fields = ['username','address','pincode']
        #fields = '__all__'
class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1']

