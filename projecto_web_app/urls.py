from django.urls import path

from projecto_web_app import views
from django.contrib import admin
from unicodedata import name
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    path('',views.home, name='Home'),
    
    
    


]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)