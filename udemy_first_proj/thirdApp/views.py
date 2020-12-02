from django.shortcuts import render
from django.http import HttpResponse
from . import forms


# Create your views here.

def form_name_view(request):
    form = forms.formName
    my_dict = {'key':form}
    return render(request,'form_pg.html', context=my_dict)



    """def sec_one(request):
    my_dictionary = {'one':'Hey buddy'}
    return render(request,'secapp.html',context=my_dictionary)"""
    