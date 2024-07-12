from django.shortcuts import redirect, render



properties = [
    {"title": "Villa Modern in Malqa", "image": "villa1.jpg"},
    {"title": "Great home for you in Rimal", "image": "villa2.jpg"},
    {"title": "Villa with 8 bedrooms in Swedey", "image": "villa3.jpg"},
    {"title": "Amazing Villa in Hitten", "image": "villa4.jpg"},


]
# Create your views here.
def home(request):
    return render(request, 'RealstateClone/home.html')



def propertiesPage(request):
    context = {
        'properties': properties,
    }
    return render(request, 'RealstateClone/properties.html', context)


def contact(request):
    return render(request,'RealstateClone/contact.html')


def home_light(request):
    response = redirect('RealstateClone:home')
    response.set_cookie('mode', 'dark', max_age=-3600)
    return response

def home_dark(request):
    response = redirect('RealstateClone:home')
    response.set_cookie('mode', 'dark', max_age=60*60*24*365*2)
    return response


# def propertiesPage_dark(request):
#     response = redirect('RealstateClone:propertiesPage')
#     response.set_cookie('dark', 'mode', max_age=60*60*24*365*2)
#     return response

# def contact_light(request):
#     response = redirect('RealstateClone:contact')
#     response.set_cookie('light', 'mode', max_age=-1000)
#     return response


# def contact_dark(request):
#     response = redirect('RealstateClone:contact')
#     response.set_cookie('dark', 'mode', max_age=60*60*24*365*2)
#     return response
