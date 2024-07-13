from django.shortcuts import render, redirect
from django.http import HttpRequest , HttpResponse


# Create your views here.
def home_views(request:HttpRequest):
    return render(request,"main/index.html")

def properties_views(request:HttpRequest)->render:
    properties = [
        {"title" : "Villa Modern in Malqa", "image" : "resources/villa1.jpg"},
        {"title" : "Great home for you in Rimal", "image" : "resources/villa2.jpg"},
        {"title" : "Villa with 8 bedrooms in Swedey", "image" : "resources/villa3.jpg"},
        {"title" : "Amazing Villa in Hitten", "image" : "resources/villa4.jpg"},
    ]
    return render(request,"main/properties.html",context={"properties": properties})
def contact_views(request:HttpRequest)->render:
    return render(request,"main/contact.html")

def dark_mode(request:HttpRequest)->render:
    response=redirect("main:home_views")
    
    response.set_cookie("dark_mode","true")
    return response
def light_mode(request:HttpRequest)->render:
    response=redirect("main:home_views")
    response.set_cookie("dark_mode","false")
    return response
