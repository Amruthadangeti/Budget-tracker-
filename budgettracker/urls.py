"""
URL configuration for budgettracker project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from .views import index
from django.urls import path , include, re_path
from django.conf.urls.static import static 
from django.conf import  settings 
from . import views

from .views import index,Goodbudget,Honeydue,pocketGuard


urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin/', admin.site.urls),
    path('',index, name='index'),
    path('Goodbudget/', Goodbudget, name='Goodbudget'),
    path('Honeydue/', Honeydue, name='Honeydue'),
    path('pocketGuard/', pocketGuard, name='pocketGuard'),


    
]


