from django.shortcuts import render
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
