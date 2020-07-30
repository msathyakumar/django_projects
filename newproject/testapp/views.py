from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect,HttpResponse
from .models import person,Family
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .forms import login_1,CreateUserForm
from django.contrib import messages


# Create your views here.

def welcome(request):
    if request.user.is_authenticated:
        details = person.objects.all()
        print(details)
        family = Family.objects.all()
        return render(request,'testapp/home.html',{'details':details,'families':family})
    else:
        messages.info(request,'please login to access this page')
        return redirect('login')

def login_form(request):
    if request.method=='POST':
        form = login_1(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('Username')
            password = form.cleaned_data.get('Password')
            print(username,password)
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                print('login successful')
                details = person.objects.all()
                family = Family.objects.all()
                family1 = Family.objects.filter(age=21)
            else:
                return redirect('login')

            return render(request,'testapp/home.html',{'details':details,'families':family})
    else:
        form = login_1()        
    return render(request,'testapp/login_page.html',{'form':form})

def logout_from(request):
    logout(request)
    return redirect('login')

def usercreate(request):
    formuser = CreateUserForm(request.POST)
    return render(request,'testapp/userlogin.html',{'form':formuser})

