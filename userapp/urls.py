from django.urls import path
from userapp import views

urlpatterns = [
    path('user_login/', views.user_login),
    path('user_reg', views.user_reg),
]