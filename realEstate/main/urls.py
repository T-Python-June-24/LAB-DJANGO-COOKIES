from django.urls import path
from . import views
app_name = "main"
urlpatterns = [
    path('',views.home_views,name="home_views"),
    path('properties/',views.properties_views,name="properties_views"),
    path("contact/",views.contact_views,name="contact_views"),
    path("light/mode/",views.light_mode,name="light_mode"),
    path("dark/mode",views.dark_mode,name="dark_mode")
    

]
