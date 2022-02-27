from cProfile import label
from django import forms



class formularioContacto(forms.Form):

    nombre = forms.CharField(label='Name',max_length=150,required=True)
    email = forms.EmailField(label='Email', required=True)
    contendo = forms.CharField(label='Content')


