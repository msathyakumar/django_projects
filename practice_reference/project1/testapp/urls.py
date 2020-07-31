from django.urls import path
from .import views

urlpatterns = [
    path('',views.home,name='home_page'),
    path('details',views.Details_view,name='details'),
    path('login',views.Login_page,name='login'),
    path('page',views.main_page,name='main_page'),
    path('logout',views.logout_view,name='logout'),

]