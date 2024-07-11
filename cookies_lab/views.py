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