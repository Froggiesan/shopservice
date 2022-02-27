from django.shortcuts import render
from .forms import formularioContacto


# Create your views here.


def contacto(request):

    formulario_contacto = formularioContacto()


    return render(request, 'contacto/contacto.html',{'miformulario':formulario_contacto})













