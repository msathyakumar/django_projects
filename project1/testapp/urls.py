from django.urls import path
from .import views

urlpatterns = [
    path('',views.home,name='home_page'),
    path('details',views.Details_view,name='details'),
    path('login',views.Login_page,name='login')

]