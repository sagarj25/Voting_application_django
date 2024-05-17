from django.contrib import admin
from django.urls import include, path
from htmlwebsite import views

app_name='htmlwebsite'

urlpatterns = [
    
path('', views.home, name='home'),
path('signn', views.sigin, name='sigin'),
path('sigup', views.sigup, name='sigup'),
path('result', views.result, name='result'),
path('about', views.about, name='about'),
path('home1', views.home1, name='home1'),
]
