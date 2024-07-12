from django.shortcuts import redirect, render
from django.http import HttpResponse


properties = [
    {"title": "Villa Modern in Malqa", "image": "villa1.jpg"},
    {"title": "Great home for you in Rimal", "image": "villa2.jpg"},
    {"title": "Villa with 8 bedrooms in Swedey", "image": "villa3.jpg"},
    {"title": "Amazing Villa in Hitten", "image": "villa4.jpg"},
]
context = {'properties': properties,}


# Create your views here.
def home(request: HttpResponse):
    """
    Renders the home page of the Real Estate website.

    Parameters:
    - request (HttpResponse): The HTTP request object.

    Returns:
    - HttpResponse: The rendered home page template.
    """
    return render(request, 'RealstateClone/home.html')



def propertiesPage(request: HttpResponse):
    """
    Renders the properties page.

    Args:
        request (HttpResponse): The HTTP request object.

    Returns:
        HttpResponse: The rendered properties page.

    """
    context = {
        'properties': properties,
    }
    return render(request, 'RealstateClone/properties.html', context)




def contact(request: HttpResponse):
    """
    Renders the contact.html template.

    Parameters:
    - request (HttpResponse): The HTTP request object.

    Returns:
    - HttpResponse: The rendered contact.html template.
    """
    return render(request, 'RealstateClone/contact.html')
def contact(request:HttpResponse):
    return render(request,'RealstateClone/contact.html')


def home_light(request: HttpResponse):
    """
    Redirects the user to the home page and sets a cookie to enable light mode.

    Args:
        request (HttpResponse): The HTTP request object.

    Returns:
        HttpResponse: The redirected response object.

    """
    response = redirect('RealstateClone:home')
    response.set_cookie('mode', 'dark', max_age=-3600)#!cookie age 
    return response

def home_dark(request: HttpResponse):
    """
    Redirects the user to the home page and sets a cookie to enable dark mode.

    Args:
        request (HttpResponse): The HTTP request object.

    Returns:
        HttpResponse: The response object with the 'mode' cookie set to 'dark'.
    """
    response = redirect('RealstateClone:home')
    response.set_cookie('mode', 'dark', max_age=60*60*24*365*2)#!cookie age 
    return response



def propertiesPage_light(request: HttpResponse):
    """
    Renders the properties page with the 'light' mode and sets a cookie.

    Args:
        request (HttpResponse): The HTTP request object.

    Returns:
        HttpResponse: The rendered properties page with the 'light' mode.

    """
    response = render(request, 'RealstateClone/propertiesPage.html', context)
    response.set_cookie('mode', 'light', max_age=-3600)#!cookie age 
    return response

def propertiesPage_dark(request: HttpResponse):
    """
    Renders the properties page with a dark mode theme and sets a cookie to remember the user's preference.

    Args:
        request (HttpResponse): The HTTP request object.

    Returns:
        HttpResponse: The rendered properties page with the dark mode theme.
    """
    response = render(request, 'RealstateClone/propertiesPage.html', context)
    response.set_cookie('mode', 'dark', max_age=60*60*24*365*2)#!cookie age 
    return response

