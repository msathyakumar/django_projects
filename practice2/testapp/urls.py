from django.urls import path
from . import views
urlpatterns =[
    path('',views.home,name='home_page'),
    path('register',views.register,name='registerform'),
    path('login',views.Login,name='login'),
    path('logout',views.logout,name='logout')
]