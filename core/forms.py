from django import forms
from django.forms import ModelForm
from django.forms import widgets
from django.forms.models import ModelChoiceField
from django.forms.widgets import Widget
from .models import Productos_Animal,Clientes , Producto
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ProductoForm(forms.ModelForm):

    class Meta: 
        model= Productos_Animal
        fields = ['id_producto', 'descripcionP', 'marca', 'imagen','categoria']
        labels ={
            'id_producto': 'ID del producto', 
            'descripcionP' :'Descripcion Producto', 
            'marca': 'Marca', 
            'imagen':'Imagen',
            'categoria': 'Categoría',
        }
        widgets={
            'id_producto': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese id', 
                    'id': 'id_producto',   
                }
            ), 
            'descripcionP': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese Descripcion', 
                    'id': 'descripcionP'
                }
            ), 
            'marca': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese marca', 
                    'id': 'marca'
                }
            ), 
            'imagen': forms.FileInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese foto del producto', 
                    'required': 'False',
                    'id': 'imagen'
                }
            ), 
            'categoria': forms.Select(
                attrs={
                    'class': 'form-control',
                    'id': 'categoria',
                }
            )

        }

class ProductoForm2(forms.ModelForm):

    class Meta: 
        model= Productos_Animal
        fields = ['id_producto', 'descripcionP', 'marca', 'imagen','categoria']
        labels ={
            'id_producto': 'ID del producto', 
            'descripcionP' :'Descripcion Producto', 
            'marca': 'Marca', 
            'imagen':'Imagen',
            'categoria': 'Categoría',
        }
        widgets={
            'id_producto': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese id', 
                    'id': 'id_producto',
                    'readonly':'readonly'
                }
            ), 
            'descripcionP': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese Descripcion', 
                    'id': 'descripcionP'
                }
            ), 
            'marca': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese marca', 
                    'id': 'marca'
                }
            ), 
            'imagen': forms.FileInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese foto del producto', 
                    'id': 'imagen'
                }
            ), 
            'categoria': forms.Select(
                attrs={
                    'class': 'form-control',
                    'id': 'categoria',
                }
            )

        }
 

 #CLIENTES

class clientesForm(forms.ModelForm):

    class Meta: 
        model= Clientes
        fields = ['rut_cliente', 'nombres_cliente', 'apellidos_clientes', 'correos_clientes','dirreciones_clientes','num_cel_clientes','sexo']
        labels ={
            'rut_cliente': 'rut del cliente', 
            'nombres_cliente' :'Nombres del cliente', 
            'apellidos_clientes': 'Apellidos cliente', 
            'correos_clientes':'Correo del cliente',
            'dirreciones_clientes': 'Direccion del cliente',
            'num_cel_clientes' : 'Numero celular cliente',
            'sexo' : 'sexo cliente',
        }
        widgets={
            'rut_cliente': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese rut', 
                    'id': 'rut_cliente',   
                }
            ), 
            'nombres_cliente': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese Nombres', 
                    'id': 'nombres_cliente'
                }
            ), 
            'apellidos_clientes': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese Apellidos', 
                    'id': 'apellidos_clientes'
                }
            ), 
            'correos_clientes': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese Correo electronico', 
                    'id': 'correos_clientes'
                }
            ), 
            'dirreciones_clientes': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese su dirrecion', 
                    'id': 'dirreciones_clientes'
                }
            ), 
            'num_cel_clientes': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese su numero celular', 
                    'id': 'num_cel_clientes'
                }
            ), 
            'sexo': forms.Select(
                attrs={
                    'class': 'form-control',
                    'id': 'sexo'
                }
            ), 


        }

class clientesForm2(forms.ModelForm):

    class Meta: 
        model= Clientes
        fields = ['rut_cliente', 'nombres_cliente', 'apellidos_clientes', 'correos_clientes','dirreciones_clientes','num_cel_clientes','sexo']
        labels ={
            'rut_cliente': 'rut del cliente', 
            'nombres_cliente' :'Nombres del cliente', 
            'apellidos_clientes': 'Apellidos cliente', 
            'correos_clientes':'Correo del cliente',
            'dirreciones_clientes': 'Direccion del cliente',
            'num_cel_clientes' : 'Numero celular cliente',
            'sexo' : 'sexo cliente',
        }
        widgets={
            'rut_cliente': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese rut', 
                    'id': 'rut_cliente',  
                    'readonly':'readonly' 
                }
            ), 
            'nombres_cliente': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese Nombres', 
                    'id': 'nombres_cliente'
                }
            ), 
            'apellidos_clientes': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese Apellidos', 
                    'id': 'apellidos_clientes'
                }
            ), 
            'correos_clientes': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese Correo electronico', 
                    'id': 'correos_clientes'
                }
            ), 
            'dirreciones_clientes': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese su dirrecion', 
                    'id': 'dirreciones_clientes'
                }
            ), 
            'num_cel_clientes': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese su numero celular', 
                    'id': 'num_cel_clientes'
                }
            ), 
            'sexo': forms.Select(
                attrs={
                    'class': 'form-control',
                    'id': 'sexo'
                }
            ), 

        }

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username',"first_name","last_name","email","password1","password2"]

class ProductoForm3(forms.ModelForm):

    class Meta: 
        model= Producto
        fields = ['codigo','nombre','imagen','marca','descripcion','precio','categoria','destacado','activo','estado']
        labels ={
            'codigo':'Codigo',
            'nombre':'Nombre del producto',
            'imagen':'Imagen de producto',
            'marca':'Marca del producto',
            'descripcion':'Descripcion del producto' ,
            'precio':'Precio del producto',
            'categoria':'Categoria del producto',
            'destacado':'destacado',
            'activo':'activo',
            'estado':'estado del pedido'
          
        }
        widgets={
            'codigo': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese id', 
                    'id': 'id_producto'
                    
                }
            ), 
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese Descripcion', 
                    'id': 'descripcionP'
                }
            ), 
            
            'imagen': forms.FileInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese foto del producto', 
                    'id': 'imagen'
                }
            ), 
            'marca': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese marca', 
                    'id': 'marca'
                }
            ), 
            'descripcion': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese marca', 
                    'id': 'marca'
                }
            ), 
            'precio': forms.NumberInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese marca', 
                    'id': 'marca'
                }
            ), 
            'categoria': forms.Select(
                attrs={
                    'class': 'form-control',
                    'id': 'categoria',
                }
            )

        }
class ProductoForm4(forms.ModelForm):

    class Meta: 
        model= Producto
        fields = ['codigo','nombre','imagen','marca','descripcion','precio','categoria','destacado','activo','estado']
        labels ={
            'codigo':'Codigo',
            'nombre':'Nombre del producto',
            'imagen':'Imagen de producto',
            'marca':'Marca del producto',
            'descripcion':'Descripcion del producto' ,
            'precio':'Precio del producto',
            'categoria':'Categoria del producto',
            'destacado':'destacado',
            'activo':'activo',
            'estado':'estado del pedido',
            
          
        }
        widgets={
            'codigo': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese id', 
                    'id': 'id_producto',
                    'readonly':'readonly'
                    
                    
                }
            ), 
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese Descripcion', 
                    'id': 'descripcionP'
                }
            ), 
            
            'imagen': forms.FileInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese foto del producto', 
                    'id': 'imagen'
                }
            ), 
            'marca': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese marca', 
                    'id': 'marca'
                }
            ), 
            'descripcion': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese marca', 
                    'id': 'marca'
                }
            ), 
            'precio': forms.NumberInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese marca', 
                    'id': 'marca'
                }
            ), 
            'categoria': forms.Select(
                attrs={
                    'class': 'form-control',
                    'id': 'categoria',
                }
            ),
            'estado': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'estado del pedido',
                }
            )

        }

        
     
 