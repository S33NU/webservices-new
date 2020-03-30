"""webservices URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views


urlpatterns = [
    path('registration/save-password',views.savePassword),
    path('registration/validate-password', views.validateClient),
    path('registration/verifyOTP', views.verifyOTP),
    path('registration/validate-phoneno',views.validatePhoneno),
    path('registration/check-password',views.checkPassword),
    path('registration/validate-email',views.validateEmail),
    path('registration/validate-password-email',views.validateClientByEmail),
    path('registration/verifyOTP-email',views.verifyOTPBByEmail),
    path('registration/check-password-email',views.checkPasswordByEmail),   
]
