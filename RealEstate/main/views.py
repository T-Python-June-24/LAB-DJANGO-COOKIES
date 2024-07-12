from django.shortcuts import render
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