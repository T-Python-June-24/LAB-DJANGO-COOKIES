from django.urls import path
from . import views 

app_name = 'houses'
urlpatterns = [
    path('',views.home, name = 'home'),
    path('properties/',views.properties, name= 'properties'),
    path('darkModeView/',views.darkModeView, name= 'darkModeView'),
    path('lightModeView/',views.lightModeView, name= 'lightModeView'),
]


