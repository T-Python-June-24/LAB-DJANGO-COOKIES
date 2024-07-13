from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('',views.home_page,name='home_page'),
    path('contact/',views.contact_page,name='contact_page'),
    path('properties/',views.properties_page,name='properties_page'),
    path('dark/',views.dark_mode,name='dark_mode'),
    path('light/',views.light_mode,name='light_mode'),
]

