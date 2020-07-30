from django.shortcuts import render,redirect
from .forms import RegisterForm,LoginForm
from .models import RegisterModel
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

# Create your views here.
def home(request):
    if request.user.is_authenticated:
        a = RegisterModel.objects.all()
        return render(request,'testapp/home.html',{'datas':a})
    else:
        return redirect('login')
def register(request):
    if request.method=='POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            id = request.POST.get('Reg_id')
            name = request.POST.get('Name')
            Branch = request.POST.get('Branch')
            obj = RegisterModel(Reg_id=id,Name=name,Branch=Branch)
            obj.save()
            a=RegisterModel.objects.all()
            print(a)
            return redirect('/')
    else:
        form = RegisterForm()
    return render(request,'testapp/register.html',{'form':form})

def Login(request):
    if request.method=='POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            name = request.POST.get('Name')
            password = request.POST.get('Password')
            user = authenticate(request,username=name,password=password)
            print('sathya')
            if user is not None:
                login(request,user)
                print('login successful')
                messages.info(request,'login successful')
            else:
                return redirect('login')     
            return render(request,'testapp/home.html')   
    else:
        form = LoginForm()
    return render(request,'testapp/login.html',{'form':form})


def Logout(request):
    logout(request)
    return redirect('login')

