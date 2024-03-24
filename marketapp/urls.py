from django.urls import path
from marketapp import views

urlpatterns = [
    path('index/', views.index),
    path('', views.index),
    path('productlist/', views.productlist),
]