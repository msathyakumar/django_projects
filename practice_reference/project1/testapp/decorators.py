from django.contrib.auth.models import User

def unauthenticated_users(view_func):
    def Wrapper_func(request,*args,**kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            view_func(request,*args,**kwargs)
    return Wrapper_func
    
