from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('register_user',views.register_user,name="register_user"),
    # path('register_ngo',views.ngo_form,name="ngo_form"),
    path('login',views.Login,name="login"),
    path('logout',views.Logout,name="logout"),

    
]