from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from firstApp import views


urlpatterns = [
    path('',views.index,name='index'),
    path('user/',views.user,name='user')
]