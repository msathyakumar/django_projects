from django.shortcuts import render
from testapp.models import Language
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType



# Create your views here.
def home(request):
    return render(request,'testapp/home.html')

def mainform(request):
    return render(request,'testapp/main.html')
