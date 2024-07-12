from . import views
from django.urls import path

app_name = "main"

urlpatterns = [
    path("", views.home_page, name="home_page"),
    path("contact/",views.contact_page,name="contact_page"),
    path("property_list/",views.property_list,name="property_list"),
    path("mode/set/dark/", views.dark_mode, name="dark_mode"),
    path("mode/set/light/", views.light_mode, name="light_mode"),


]