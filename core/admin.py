from django.contrib import admin
from .models import CategoriaAnimal, Clientes,Productos_Animal,SexoCliente ,Producto ,Categoria
# Register your models here.

admin.site.register(CategoriaAnimal)
admin.site.register(Categoria)
admin.site.register(Productos_Animal)
admin.site.register(Producto)
admin.site.register(SexoCliente)
admin.site.register(Clientes)

