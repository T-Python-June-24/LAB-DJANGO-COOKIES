from django.shortcuts import render
from django.http import HttpRequest,HttpResponse

def home_view(request:HttpRequest):

    print(request.COOKIES)
    
    response = render(request, "home.html")
    response.set_cookie("dark", "mode", max_age=3500)

    return response

def properties_view(request:HttpRequest):
    properties = [
        {"title" : "Villa Modern in Malqa", "image" : "villa1.jpg"},
        {"title" : "Great home for you in Rimal", "image" : "villa2.jpg"},
        {"title" : "Villa with 8 bedrooms in Swedey", "image" : "villa3.jpg"},
        {"title" : "Amazing Villa in Hitten", "image" : "villa4.jpg"}
    ]

    return render(request, "properties.html", context={"properties":properties})

def contact_view(request:HttpRequest):
    
    return render(request, "contact.html")



