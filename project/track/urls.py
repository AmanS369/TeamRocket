from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.home,name='home'),

    path('register_user',views.register_user,name="register_user"),
    path('login',views.Login,name="login"),
    path('logout',views.Logout,name="logout"),
    path('dashboard',views.dashboard,name="dashboard"),
    path('event_dashboard',views.event_dashboard,name="event_dashboard"),
    path('achievment',views.achievment,name="achievment"),
    path('<str:input>/', views.landing_page, name='landing_page'),
    
    
]