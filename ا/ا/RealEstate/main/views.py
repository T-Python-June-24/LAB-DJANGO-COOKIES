from django.shortcuts import render
from .models import Property
from django.shortcuts import render

def properties(request):
   properties = [
      {"title": "Villa Modern in Malqa", "image": "villa1.jpg"},
      {"title": "Great home for you in Rimal", "image": "villa2.jpg"},
      {"title": "Villa with 8 bedrooms in Swedey", "image": "villa3.jpg"},
      {"title": "Amazing Villa in Hitten", "image": "villa4.jpg"},
    ]
   return render(request, 'main/properties.html', {'properties': properties})



def services(request):
    return render(request, 'main/services.html')

def about(request):
    properties = [
        {"title": "Villa Modern in Malqa", "image": "villa1.jpg"},
        {"title": "Villa with 8 bedrooms in Swedey", "image": "villa3.jpg"},
        {"title": "Amazing Villa in Hitten", "image": "villa4.jpg"},
    ]
    return render(request, 'main/about.html', {'properties': properties})

def contact(request):
    return render(request, 'main/contact.html')

# main/views.py




def home(request):
    return render(request, 'main/home.html')
