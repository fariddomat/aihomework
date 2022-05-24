from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("storeCountry", views.storeCountry, name="storeCountry"),
    path("romania", views.romania, name="romania"),
    
]
