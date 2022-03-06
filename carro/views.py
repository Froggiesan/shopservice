from django.shortcuts import render
from .carro import carro
from tienda.models import Producto
from django.shortcuts import redirect

# Create your views here.


# view to add items
def agregar_producto(request,producto_id):
    carroz = carro(request)

    producto = Producto.objects.get(id=producto_id)

    carroz.agregar(producto=producto)

    return redirect('Tienda')

# view to delete 1 product
def eliminar_producto(request,producto_id):
    carroz = carro(request)

    producto = Producto.objects.get(id=producto_id)

    carroz.eliminar(producto=producto)
    
    return redirect('Tienda')
    
#view to subtract
def restar_producto(request,producto_id):
    carroz = carro(request)

    producto = Producto.objects.get(id=producto_id)

    carroz.restar_producto(producto=producto)
    
    return redirect('Tienda')
#view to clean it
def limpiar_carro(request, producto_id):
    carroz = carro(request)

    carroz.limpiar_carro()

    return redirect('Tienda')