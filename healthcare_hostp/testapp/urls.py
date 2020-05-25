from django.urls import path
from . import views

urlpatterns =[
    path('',views.home_page,name='home_page'),
    path('information',views.information_page,name='information_page'),
    path('login',views.login_form_,name='login_form'),
    path('register',views.registration_form,name='register_form'),
    path('mainform',views.mainform_in_login,name='mainform'),
    path('patient',views.patient_details,name='patient'),
    path('prescriptions',views.prescription,name='prescriptions')
]