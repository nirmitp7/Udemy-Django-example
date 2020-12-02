from django.shortcuts import render
from django.http import HttpResponse
from firstApp.models import Topic, Webpage, AccessRecord, User

# Create your views here.

def index(request):

    webpages_list= AccessRecord.objects.order_by('date')
    my_dict = {'key_one':webpages_list}
    return render(request,'firstapp.html',context=my_dict)


def user(request):
    usr = User.objects.order_by('first_nm')
    dictn = {'k_one':usr}
    return render(request,'proj_one.html',context=dictn)