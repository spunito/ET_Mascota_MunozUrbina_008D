
from itertools import product
from django.contrib import messages
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Clientes, Productos_Animal ,Producto,Categoria
from .forms import ProductoForm ,ProductoForm2, clientesForm, clientesForm2 ,CustomUserCreationForm ,ProductoForm3,ProductoForm4
from django.contrib.auth import authenticate , login
from django.contrib.auth.decorators import login_required , permission_required
from django.contrib.sessions.models import Session
import os

# Create your views here.
TEMPLATES_DIRS=(
    'os.path.join(BASE_DIR, "templates"),'
)

def index(request):
    return render(request, "index.html")
def somos(request):
    return render(request ,"somos.html")
def exitosa(request):
    return render(request,"exitosa.html")
def pedidos(request):
    return render(request,"pedidos.html")

#Carrito de compra 
def galeria(request):
    
    categorias=Categoria.objects.filter(activo = True)
    productos= Producto.objects.filter(activo = True)
    context ={"productos":productos,"categorias":categorias}
    return render(request ,"galeria.html",context)

def detail(request,slug):
    if Producto.objects.filter(activo=True , slug=slug).exists():
        product =Producto.objects.get(activo=True , slug=slug)
        categorias =Categoria.objects.filter(activo=True )
        context ={"product":product,"categorias":categorias}
        return render(request ,"detail.html",context)

def cart(request,slug):
    product = Producto.objects.get(slug=slug)
    initial ={"items":[],"price":0,"count":0}
    session=request.session.get("data",initial)
    if slug in session["items"]:
        messages.error(request,"Producto ya existe en el carrito")
    else:
        session["items"].append(slug)
        session["price"] +=int(product.precio)
        session["count"]+=1
        request.session["data"]=session
        messages.success(request,"Agregado exitosamente")
    return redirect("detail",slug)

def mycart(request):
    sess = request.session.get("data",{"items":[]})
    products =Producto.objects.filter(activo=True,slug__in=sess["items"])
    categorias = Categoria.objects.filter(activo=True)
    context ={"products":products,"categorias":categorias}
    return render(request ,"lista.html",context)

def pedido(request):
    sess = request.session.get("data",{"items":[]})
    products =Producto.objects.filter(activo=True,slug__in=sess["items"])
    categorias = Categoria.objects.filter(activo=True)
    context ={"products":products,"categorias":categorias}
    return render(request ,"pedido.html",context)

#Termino carrito de compra
def contacto(request):
    return render(request,"contacto.html")
def mapa(request):
    return render(request ,"maps.html")
def dogApi(request):
    return render(request,"dogsAPI.html")

def noCuenta(request):
    return render(request , "no_cuenta.html")

def registrar(request):
    data = {
        'form': CustomUserCreationForm()
    }

    if request.method == 'POST' :
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            return redirect('index')
        data["form"] = formulario
    return render(request , 'registration/registrar.html', data)

#Termino Templates normales - Inicia Templates CRUD

@permission_required('core.view_productos_animal')
def mostrar(request):
    productos = Producto.objects.all()

    datos = {
        'productos': productos
    }
    return render(request, 'mostrar.html', datos)
@permission_required('core.add_productos_animal')
def form_producto(request):
    if request.method=='POST': 
        producto_form = ProductoForm3(request.POST, request.FILES)
        if producto_form.is_valid():
            producto_form.save()
            return redirect('mostrar')
    else:
        producto_form=ProductoForm3()
    return render(request, 'form_crear_producto.html', {'producto_form': producto_form})
@permission_required('core.change_productos_animal')
def form_mod_producto(request, id): 
    producto = Producto.objects.get(codigo=id)
    datos = {
        'producto_form': ProductoForm4(instance=producto)
    }
    if request.method=='POST':
        if len(request.FILES) != 0:
            if len(producto.imagen) > 0:
                os.remove(producto.imagen.path)
        formulario = ProductoForm3(data = request.POST, instance=producto)
        if formulario.is_valid: 
            formulario.save()
            return redirect ('mostrar')
    return render (request, 'form_mod_producto.html', datos )
@permission_required('core.delete_productos_animal')
def form_del_producto(request, id):
    producto = Producto.objects.get(codigo=id)
    producto.delete()
    return redirect('mostrar')


#CLIENTES
@permission_required('core.view_clientes')
def mostrar1(request):
    cliente = Clientes.objects.all()
    datos = {
        'clientes': cliente
    }
    return render(request, 'mostrar_clientes.html', datos)
@permission_required('core.add_clientes')
def form_clientes(request):
    if request.method=='POST': 
        clientes_form = clientesForm(request.POST)
        if clientes_form.is_valid():
            clientes_form.save()
            return redirect('index')
    else:
        clientes_form= clientesForm()
    return render(request, 'form_crear_clientes.html', {'clientes_form': clientes_form})

@permission_required('core.change_clientes')
def form_mod_clientes(request, id): 
    cliente = Clientes.objects.get(rut_cliente=id)
    datos = {
        'form': clientesForm2(instance=cliente)
    }
    if request.method=='POST':
        formulario = clientesForm2(data = request.POST, instance=cliente)
        if formulario.is_valid: 
            formulario.save()
            return redirect ('mostrar_clientes')
    return render (request, 'form_mod_clientes.html', datos )
@permission_required('core.delete_clientes')
def form_del_clientes(request, id):
    cliente = Clientes.objects.get(rut_cliente=id)
    cliente.delete()
    return redirect('mostrar_clientes')




