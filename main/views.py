from django.shortcuts import redirect, render
from django.http import HttpRequest, HttpResponse
from .algorithm import  searchAlgorithm
# Create your views here.



def index(response):
    data=""
    data2=""
    
    if response.method=="POST":
        # search_form=response.POST
        data = searchAlgorithm(response.POST.getlist("start"),response.POST.getlist("goal"))
    else:
        search_fields=''
    return render(response,'main/index.html', {"data":data})
