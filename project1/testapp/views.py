from django.shortcuts import render,redirect
from .forms import Details_form,UserForm

# Create your views here.
def home(request):
    return render(request,'testapp/home.html')


def Details_view(request):
    form= Details_form()
    return render(request,'testapp/details_log.html',{'form':form})
def Login_page(request):
    form = UserForm()
    return render(request,'testapp/login.html',{'form':form})
        

