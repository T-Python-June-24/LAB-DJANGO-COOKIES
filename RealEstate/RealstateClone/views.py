from django.shortcuts import redirect, render
from django.http import HttpRequest,HttpResponse


properties = [
    {"title": "Villa Modern in Malqa", "image": "villa1.jpg"},
    {"title": "Great home for you in Rimal", "image": "villa2.jpg"},
    {"title": "Villa with 8 bedrooms in Swedey", "image": "villa3.jpg"},
    {"title": "Amazing Villa in Hitten", "image": "villa4.jpg"},


]
# Create your views here.
def home(request:HttpResponse):
    return render(request, 'RealstateClone/home.html')



def propertiesPage(request:HttpResponse):
    context = {
        'properties': properties,
    }
    return render(request, 'RealstateClone/properties.html', context)


def contact(request:HttpResponse):
    return render(request,'RealstateClone/contact.html')


def home_light(request:HttpResponse):
    response = redirect('RealstateClone:home')
    response.set_cookie('mode', 'dark', max_age=-3600)
    return response

def home_dark(request:HttpResponse):
    response = redirect('RealstateClone:home')
    response.set_cookie('mode', 'dark', max_age=60*60*24*365*2)
    return response



def propertiesPage_light(request:HttpResponse):
    context = {
        'properties': properties,
    }
    
    response = render(request, 'RealstateClone/propertiesPage.html', context)
    response.set_cookie('mode', 'light', max_age=60*60*24*365*2)
    return response

def propertiesPage_dark(request:HttpResponse):
    context = {
        'properties': properties,
    }
    
    response = render(request, 'RealstateClone/propertiesPage.html', context)
    response.set_cookie('mode', 'dark', max_age=60*60*24*365*2)
    return response

