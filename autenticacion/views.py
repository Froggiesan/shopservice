from django.shortcuts import redirect, render
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout,authenticate
import autenticacion
from django.contrib import messages


# Create your views here.

class vRegistro(View):


    def get(self, request):
        form = UserCreationForm()
        return render(request, "autenticacion/autenticacion.html",{"form":form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        

        
        if form.is_valid():
            usuario = form.save()
            
            login(request,usuario)

            return redirect('Home')
        else:
            for msg in form.error_messages:
                messages.error(request,form.error_messages[msg])
            
            return render(request, "autenticacion/autenticacion.html",{"form":form})

def close_session(request):
    #Now we close the session.
    logout(request)
    # Redirect to the home page
    return redirect('Home')

def logear(request):
    if request.method =="POST":
        form =  AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            userna_name = form.cleaned_data.get("username")
            password2 = form.cleaned_data.get("password")
            usuario = authenticate(username=userna_name, password=password2)
            if usuario is not None:
                login(request,usuario)
                return redirect('Home')
            else:
                messages.error(request,"Invalid user")
        else:
                messages.error(request,"Invalid user")

    form =  AuthenticationForm()
    return render(request, "login/login.html",{"form":form})



        
