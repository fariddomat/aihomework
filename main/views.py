from django.shortcuts import redirect, render
from django.http import HttpRequest, HttpResponse
from .forms import SearchAlgorithm,StoreNewCountry
from .algorithm import  searchAlgorithm, storeNewMap,SetRomaniaMap
# Create your views here.



def index(response):
    data=""
    data2=""
    if response.method=="POST":
        search_fields=SearchAlgorithm(response.POST)
        store_fields=StoreNewCountry()
        if search_fields.is_valid():
            data = searchAlgorithm(search_fields.cleaned_data["start_city"],search_fields.cleaned_data["end_city"])   
    else:
        search_fields=SearchAlgorithm()
        store_fields=StoreNewCountry()
    return render(response,'main/index.html', {"search_fields":search_fields,"store_fields":store_fields, "data":data, "data2":data2})

def storeCountry(response):
    data=""
    data2=""
    if response.method=="POST":
        store_fields=StoreNewCountry(response.POST)
        search_fields=SearchAlgorithm()
        if store_fields.is_valid():
            data2 = storeNewMap(store_fields.cleaned_data["cities"],store_fields.cleaned_data["heuristics"])  
    else:
        search_fields=SearchAlgorithm()
        store_fields=StoreNewCountry()
    return render(response,'main/index.html', {"search_fields":search_fields,"store_fields":store_fields, "data":data, "data2":data2})

def romania(response):
    date=""
    date=SetRomaniaMap()
    return redirect('index')