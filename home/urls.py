
from django.urls import path
from .views import login_principal, redirigir_login

urlpatterns = [
    path('login-principal/', login_principal, name='login_principal'),
    path('redirigir-login/', redirigir_login, name='redirigir_login'),
   
]
