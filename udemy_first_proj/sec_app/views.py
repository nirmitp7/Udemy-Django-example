from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('Hey this is second App')


def sec_one(request):
    my_dictionary = {'one':'Hey buddy'}
    return render(request,'secapp.html',context=my_dictionary)