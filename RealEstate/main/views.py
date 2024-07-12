from django.shortcuts import render
from django.http import HttpRequest,HttpResponse

def home_view(request:HttpRequest):

    print(request.COOKIES)
    
    response = render(request, "home.html")
    response.set_cookie("Abdulaziz", "The best Thinker")

    return response

def properties_view(request:HttpRequest):
    return render(request, "properties.html")

def contact_view(request:HttpRequest):
    return render(request, "contact.html")



