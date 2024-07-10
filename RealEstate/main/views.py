from django.shortcuts import render
from django.http import HttpRequest,HttpResponse

def home_view(request:HttpRequest):
    return render(request, "home.html")

def properties_view(request:HttpRequest):
    pass

def contact_view(request:HttpRequest):
    pass



