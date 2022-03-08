from django.urls import path
from .views import vRegistro


urlpatterns = [
    
    path('',vRegistro.as_view(), name='Autenticacion'),
    
    
    
    


]

