from pyexpat import model
from django.db import models
from django_extensions.db.fields import AutoSlugField

# Create your models here.

class CategoriaAnimal(models.Model):
    idCategoriaA = models.IntegerField(primary_key=True, verbose_name='Id de Categoria')
    nombreCategoriaA=models.CharField(max_length=50, verbose_name='Nombre de Categoria Animal')

    def __str__(self): 
        return self.nombreCategoriaA


class Productos_Animal (models.Model): 
    id_producto = models.CharField(primary_key=True, max_length=6, verbose_name='id_producto')
    descripcionP= models.CharField(max_length=60, verbose_name='Descripcion')
    marca= models.CharField(max_length=20, verbose_name='Marca') 
    imagen =models.ImageField(upload_to="productos",null=True)
    categoria = models.ForeignKey(CategoriaAnimal, on_delete=models.CASCADE, verbose_name='Categoria Animal')
    
    def __str__(self):
        return self.descripcionP

class Categoria(models.Model):
    nombre = models.CharField (max_length=250 ,verbose_name='Id de Categoria')
    slug = AutoSlugField(populate_from="nombre")
    activo=models.BooleanField(default=True)

    def __str__(self) -> str : 
        return self.nombre


class Producto (models.Model): 
    codigo = models.CharField(primary_key=True, max_length=10, verbose_name='codigo')
    nombre = models.CharField(max_length=250, verbose_name='nombre')
    slug = AutoSlugField(populate_from="nombre")
    imagen =models.ImageField(upload_to="productos",null=True)
    marca= models.CharField(max_length=20, verbose_name='Marca') 
    descripcion = models.TextField(blank=True,null=True)
    precio = models.PositiveIntegerField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, verbose_name='Categoria')
    destacado = models.BooleanField(default=True)
    activo = models.BooleanField(default=True)
    estado = models.CharField(max_length=20, verbose_name='Estado')
    def __str__(self) -> str : 
        return self.nombre
    

class SexoCliente(models.Model):
    idsexo = models.IntegerField(primary_key=True, verbose_name='Id de sexo')
    nombreSexo=models.CharField(max_length=50, verbose_name='Nombre de sexo')

    def __str__(self): 
        return self.nombreSexo


class Clientes(models.Model):
    rut_cliente=models.CharField(primary_key=True, max_length=10, verbose_name='rut_cliente')
    nombres_cliente=models.CharField(max_length=30, verbose_name='Nombres')
    apellidos_clientes=models.CharField(max_length=30, verbose_name='Apellidos')
    correos_clientes=models.CharField(max_length=30, verbose_name='Correos')
    dirreciones_clientes=models.CharField(max_length=30, verbose_name='Dirreción')
    num_cel_clientes=models.CharField(max_length=30, verbose_name='Número de celular')
    sexo = models.ForeignKey(SexoCliente, on_delete=models.CASCADE, verbose_name='Sexo cliente')
    
  
    def __str__(self):
        return self.rut_cliente

        