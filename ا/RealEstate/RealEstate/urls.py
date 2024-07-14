# RealEstate/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('main.urls')),  # Include your app's URLs here
    path('admin/', admin.site.urls),
]


