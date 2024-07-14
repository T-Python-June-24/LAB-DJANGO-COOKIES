from . import views
from django.urls import path

app_name = "RealEstate"

urlpatterns = [
    path('', views.home_view, name="home"),
    path('properties/', views.properties_view, name="properties"),
    path('contact/', views.contact_view, name="contact"),
    path('dark-mode/', views.dark_mode_view, name="dark_mode"),
    path('light-mode/', views.light_mode_view, name="light_mode"),
]
