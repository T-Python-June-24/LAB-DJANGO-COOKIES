from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse

# Create your views here.
def home_view(request: HttpRequest):
  return render(request, "main/index.html")

def properties_view(request: HttpRequest):
  return render(request, "main/properties.html")

def contact_view(request: HttpRequest):
  return render(request, "main/contact.html")

def dark_view(request: HttpRequest):
  response = redirect("main:home_view")
  response.set_cookie("mode", "dark", max_age=60*60*24)
  return response

def light_view(request: HttpRequest):
  response = redirect("main:home_view")
  response.set_cookie("mode", "light", max_age=-3600)

  return response