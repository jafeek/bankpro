"""
URL configuration for bellbankpro project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
from .views import index
urlpatterns = [
    path('',views.home,name="index"),

    path('registration',views.registration,name="registration"),
    path('login',views.login,name="login"),
    path('branches',views.branches,name="branches"),
    path('Rform',views.Rform,name="Rform"),
    path('logout',views.logout,name="index"),
    path('message',views.message,name='message'),
    path('dropdown',views.dropdown,name="dropdown")



]
