from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # Authentication
    path('accounts/', include('django.contrib.auth.urls')),  #this is for  gives login/logout
    path('', views.dashboard, name='dashboard'),
    path('vaccines/', views.vaccine_list, name='vaccine_list'),
    path('vaccines/create/', views.vaccine_create, name='vaccine_create'),
]
