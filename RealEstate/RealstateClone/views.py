from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'RealstateClone/home.html')


properties = [
    {"title": "Villa Modern in Malqa", "image": "villa1.jpg"},
    {"title": "Great home for you in Rimal", "image": "villa2.jpg"},
    {"title": "Villa with 8 bedrooms in Swedey", "image": "villa3.jpg"},
    {"title": "Amazing Villa in Hitten", "image": "villa4.jpg"},


]

# Create your views here.
def propertiesPage(request):
    context = {
        'properties': properties,
    }
    return render(request, 'RealstateClone/properties.html', context)


def contact(request):
    return render(request,'RealstateClone/contact.html')

