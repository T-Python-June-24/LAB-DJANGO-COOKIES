from django.shortcuts import render

def home(request):

    return render(request, "main/home.html")

def properties(request):

    return render(request, "main/properties.html")

def contact(request):

    return render(request, "main/contact.html")
