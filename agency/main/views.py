from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse

def home(request: HttpRequest):

    response = render(request, "main/home.html")
    return response

def properties(request: HttpRequest):

    return render(request, "main/properties.html")

def contact(request: HttpRequest):

    return render(request, "main/contact.html")

def light(request: HttpRequest):

    response = redirect("main:home")
    response.set_cookie("mode","light", max_age=60*60*24)
    return response

def dark(request: HttpRequest):

    response = redirect("main:home")
    response.set_cookie("mode","dark", max_age=60*60*24)
    return response