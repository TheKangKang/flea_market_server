from django.contrib import admin
from django.urls import path, include

from marketapp import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('marketapp.urls')),
    path('', include('userapp.urls')),
]
