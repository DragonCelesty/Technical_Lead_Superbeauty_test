from django.contrib import admin
from django.urls import path
from .views import Index, SingUpView, Dashboard, Equipment_APIView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('singup/', SingUpView.as_view(), name='singup'),
    path('login/', auth_views.LoginView.as_view(template_name='inventory/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='inventory/logout.html'), name='logout'),
    path('dashboard/', Dashboard.as_view(), name='dashboard'),
    path('api/equipment/', Equipment_APIView.as_view(), name='getEquipment')
]
