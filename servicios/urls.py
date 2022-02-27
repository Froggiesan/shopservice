from django.urls import path
from . import views
from django.contrib import admin
from unicodedata import name
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    path('servicios',views.servicios, name='Servicios'),
    
    


]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)