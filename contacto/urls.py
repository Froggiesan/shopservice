from django.urls import path

from autenticacion.views import close_session
from . import views



urlpatterns = [
    
    path('',views.contacto, name='Contacto'),
    

    


]
