from django.urls import path

from . import views

app_name = 'main'
urlpatterns = [
    path('', views.home_view, name='home_view'),
    path('properties/', views.properties_view, name='properties_view'),
    path('contact/', views.contact_view, name='contact_view'),
    path("mode/light/", views.light_mode_view, name="light_mode_view"),
    path("mode/dark/", views.dark_mode_view, name="views.dark_mode_view"),
]
