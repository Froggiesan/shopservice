from django.db import models

# Create your models here to create BD in SQLite
class categoriaProducto(models.Model):
    nombre = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name = 'categoriaProducto'
        verbose_name_plural = 'categoriasProducto'
    
    def __str__(self):
        return self.nombre


class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    categorias = models.ForeignKey(categoriaProducto,on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to = 'tienda', null = True, blank=True)
    precio = models.FloatField()
    disponibilidad = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'


