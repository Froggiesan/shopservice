from django.contrib import admin

from blog.admin import CategoriaAdmin
from .models import categoriaProducto,Producto
# Register your models here.

class categoriaProductoAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')

class ProductoAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')


admin.site.register(categoriaProducto,categoriaProductoAdmin)

admin.site.register(Producto,ProductoAdmin)