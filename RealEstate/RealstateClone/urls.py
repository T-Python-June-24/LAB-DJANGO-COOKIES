from . import views
from django.urls import path

app_name = 'RealstateClone'
urlpatterns = [
    path('', views.home, name='home'),
    path('properties/',views.propertiesPage,name='properties'),
    path('contact/',views.contact,name='contact')
]