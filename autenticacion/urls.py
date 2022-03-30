from django.urls import path
from .views import vRegistro,close_session,logear


urlpatterns = [
    
    path('',vRegistro.as_view(), name='Autenticacion'),
    path('close_session',close_session, name='close_session'),
    path('logear',logear, name='logear'),

    
    
    
    


]

