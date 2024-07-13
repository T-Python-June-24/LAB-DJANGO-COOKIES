from django.shortcuts import render, redirect
from django.http import HttpRequest , HttpResponse 

def home_page(request:HttpRequest):
    
    return render(request,'main/index.html')

def contact_page(request:HttpRequest):
    
    return render(request,'main/contact.html')


def properties_page(request:HttpRequest):

    properties = [
        {"title" : "Villa Modern in Malqa", "image" : "images/villa1.jpg"},
        {"title" : "Great home for you in Rimal", "image" : "images/villa2.jpg"},
        {"title" : "Villa with 8 bedrooms in Swedey", "image" : "images/villa3.jpg"},
        {"title" : "Amazing Villa in Hitten", "image" : "images/villa4.jpg"},
    ]
    
    response = render(request,'main/properties.html',{'properties_list':properties})

    return response

def dark_mode(request:HttpRequest):

    response =  redirect(request.META.get('HTTP_REFERER', '/'))  
    response.set_cookie("mode","dark",max_age=60*60*24*7)

    return response

def light_mode(request:HttpRequest):

    response =  redirect(request.META.get('HTTP_REFERER', '/'))  
    response.delete_cookie("mode")

    return response
