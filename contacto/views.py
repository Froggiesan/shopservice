from django.shortcuts import redirect, render
from .forms import formularioContacto
from django.core.mail import EmailMessage

# Create your views here.


def contacto(request):

    formulario_contacto = formularioContacto()

    if request.method == 'POST':
        formulario_contacto = formularioContacto(data=request.POST)

        if formulario_contacto.is_valid():
            nombre = request.POST.get("nombre")
            email = request.POST.get("email")
            contenido = request.POST.get("contendo")


            email = EmailMessage('Message of our page',
            'User name {} ,email: {} ,writes: \n\n {}'.format(nombre,email,contenido),
            '',['pruebasdjangopildoras@gmail.com'],reply_to=[email])
            
            

            try:
                email.send()
                
                return redirect("/contacto/?valido")
            except:
                return redirect("/contacto/?novalido")




    return render(request, 'contacto/contacto.html',{'miformulario':formulario_contacto})
















