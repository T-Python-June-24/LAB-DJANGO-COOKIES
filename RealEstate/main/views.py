from django.shortcuts import render ,redirect
from django.http import HttpRequest,HttpResponse

def home_page(request):
    return render(request, "main/index.html")
def contact_page(request):
    return render(request, "main/contact.html")

def property_list(request):
    properties = [
        {"title": "Villa Modern in Malqa", "image": "images/villa1.jpg"},
        {"title": "Great home for you in Rimal", "image": "images/villa2.jpg"},
        {"title": "Villa with 8 bedrooms in Swedey", "image": "images/villa3.jpg"},
        {"title": "Amazing Villa in Hitten", "image": "images/villa4.jpg"},
    ]
    return render(request, 'main/properties.html', {'properties': properties})


from django.shortcuts import redirect

def dark_mode(request):
    response = redirect(request.META.get('HTTP_REFERER', '/'))  
    response.set_cookie("mode", "dark", max_age=60*60*24*365)  
    return response

def light_mode(request):
    response =  redirect(request.META.get('HTTP_REFERER', '/'))  
    response.delete_cookie("mode")
    return response