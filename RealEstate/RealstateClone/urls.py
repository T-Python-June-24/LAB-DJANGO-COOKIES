from . import views
from django.urls import path

app_name = 'RealstateClone'
urlpatterns = [
    path('', views.home, name='home'),
    path('properties/', views.propertiesPage, name='properties'),
    path('contact/', views.contact, name='contact'),
    path('home_light/', views.home_light, name='home_light'),
    path('home_dark/', views.home_dark, name='home_dark'),
    path('properties_light/', views.propertiesPage_light, name='properties_light'),
    path('properties_dark/', views.propertiesPage_dark, name='properties_dark'),
]
