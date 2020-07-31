from django.shortcuts import render,redirect
from .forms import Details_form,UserForm,loginform_1
from django.contrib import messages
from django.contrib.auth import login,authenticate,logout

# Create your views here.
def home(request):
    messages.info(request,'home page info')
    messages.success(request,'success message')
    return render(request,'testapp/home.html')


def Details_view(request):
    form= Details_form()
    return render(request,'testapp/details_log.html',{'form':form})


def Login_page(request):
    if request.method=='POST':
        form = loginform_1(request.POST)
        if form.is_valid():
            username= form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username,password=password)
            print(user)
            print(username,password)
            if user is not None:
                login(request,user)
                messages.success(request,'login successful')
                return redirect('page')
        else:
            messages.info(request,'form is in valid')
    else:
        form= print(username,password)
    return render(request,'testapp/login.html',{'form':form})

def main_page(request):
    return render(request,'testapp/main_page.html')

def logout_view(request):
    logout(request)
    return render(request,'testapp/login.html')    
