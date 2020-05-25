from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from.models import PATIENT


# Create your views here.
def home_page(request):
    return render(request,'testapp/home.html')


def information_page(request):
    return render(request,'testapp/info.html')

def login_form_(request):
    if request.method=='POST':
        password = request.POST['password']
        username = request.POST['user_name']
        user=None
        user = auth.authenticate(username= username,password = password)
        if user is None:
            auth.login(request,user)
            print('login successful')
            return redirect('mainform')
        else:
            print('data not sufficient')
            return render(request,'testapp/login.html',{'name':'user not exist'})
    else:
        return render(request,'testapp/login.html')


def registration_form(request):
    if request.method=="POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        username = request.POST['username']
        if password1==password2:
            if User.objects.filter(username=username).exists():
                print('useralready exist')
                
                return render(request,'testapp/register.html',{'name':'user already exist'})
            elif User.objects.filter(email=email).exists():
                print('email exist')
                return render(request,'testapp/register.html',{'name':'email already exist'})
            else:
                user = User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
                user.save();
                print('user created')
            return redirect('/')
        else :
            print('password is incorrect')
            return render(request,'testapp/register.html',{'name':'password didnot match'})
    
    else:
        return render(request,'testapp/register.html')


def mainform_in_login(request):
    return render(request,'testapp/mainform.html')



def patient_details(request):
    users = PATIENT.objects.all()
    print(users)
    #user = PATIENT(5,'NEW','NAME')
    return render(request,'testapp/patient.html',{'users':users})
    

def prescription(request):
    return render(request,'testapp/prescriptions.html')