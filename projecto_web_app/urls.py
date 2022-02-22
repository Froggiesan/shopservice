from django.urls import path
from projecto_web_app import views
from django.contrib import admin
from unicodedata import name



urlpatterns = [
    
    path('',views.home, name='Home'),
    path('servicios',views.servicios, name='Servicios'),
    path('tienda',views.tienda, name='Tienda'),
    path('blog',views.blog, name='Blog'),
    path('contacto',views.contacto, name='Contacto'),



]