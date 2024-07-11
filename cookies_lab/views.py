from django.shortcuts import render, redirect


# Create your views here.

def index(request):
    response = render(request, 'cookies_lab/index.html', )
    return response

def dark_mode(request):
    response = redirect('cookies_lab:index')
    response.set_cookie('mode', 'dark', max_age=60*60*24*30)
    return response

def light_mode(request):
    response = redirect('cookies_lab:index')
    response.delete_cookie('mode')
    return response

def properties(request):
    properties = [
        {"title" : "Villa Modern in Malqa", "image" : "villa1.jpg"},
        {"title" : "Great home for you in Rimal", "image" : "villa2.jpg"},
        {"title" : "Villa with 8 bedrooms in Swedey", "image" : "villa3.jpg"},
        {"title" : "Amazing Villa in Hitten", "image" : "villa4.jpg"},
    ]
    response = render(request, 'cookies_lab/properties.html', {"properties" : properties})
    return response

def contact(request):
    response = render(request, 'cookies_lab/contact.html')
    return response