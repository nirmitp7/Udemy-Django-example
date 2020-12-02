
from django.contrib import admin
from django.urls import path
from thirdApp import views

urlpatterns = [
    path('form/',views.form_name_view,name='form_name_view')
]