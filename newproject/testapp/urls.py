from django.urls import path
from . import views

urlpatterns =[
    path('',views.welcome,name='welcome'),
    path('login',views.login_form,name='login'),
    path('logout',views.logout_from,name='logout'),
    path('userlogin',views.usercreate,name='userlogin'),
]