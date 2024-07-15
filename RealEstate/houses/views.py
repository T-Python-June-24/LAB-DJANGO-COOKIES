from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
# Create your views here.



def home(request: HttpRequest):
    response = render(request, 'houses/home.html')
    response.set_cookie('name','value')
    return response

def properties(request: HttpRequest):
    properties = [
        {"title" : "Villa Modern in Malqa", "image" : "villa1.jpg"},
        {"title" : "Great home for you in Rimal", "image" : "villa2.jpg"},
        {"title" : "Villa with 8 bedrooms in Swedey", "image" : "villa3.jpg"},
        {"title" : "Amazing Villa in Hitten", "image" : "villa4.jpg"},
    ]
    return render(request, 'houses/properties.html', context={'properties': properties})


def darkModeView(request:HttpRequest):
    response = redirect("houses:home")
    response.set_cookie("mode","dark",max_age=60*60*24)
    return response

def lightModeView(request:HttpRequest):
    response = redirect("houses:home")
    response.set_cookie("mode","light",max_age= -3600)
    return response