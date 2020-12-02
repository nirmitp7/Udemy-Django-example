from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from sec_app import views


urlpatterns = [
    path('',views.sec_one,name='sec_one')

]