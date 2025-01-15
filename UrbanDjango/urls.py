"""
URL configuration for UrbanDjango project.

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
from django.contrib import admin
from django.core.management.commands.runserver import naiveip_re
from django.urls import path, include
from task2.views import class_based_view, function_based_view
#from task3.views import main_page, second_page, third_page
#from task4.views import main_page, second_page, third_page
from task5.views import sign_up_by_html, sign_up_by_django

urlpatterns = [
    path('', sign_up_by_html, name='html_sign_up'),
    path('django/', sign_up_by_django, name='djanjo_sign_up'),
    #path('', main_page),
    #path('main-page/', main_page, name='main_page'),
    #path('second-page/', second_page, name='second_page'),
    #path('third-page/', third_page, name='third_page'),
    #path('class-view/', class_based_view, name='class_view'),
    #path('function-view/', function_based_view, name='function_view'),
]
