from django.urls import path
from .views import form_clientes, pedido,form_del_clientes,detail,form_mod_clientes,cart,mycart, registrar,index, mostrar1,somos,galeria,contacto,dogApi,login,mapa,noCuenta,form_del_producto,form_mod_producto,mostrar,form_producto,exitosa



urlpatterns = [
    path('', index , name="index"),
    path('somos/',somos,name="somos"),
    path('galeria/',galeria,name="galeria"),
    path('contacto/',contacto,name="contacto"),
    path('mapa/',mapa,name="mapa"),
    path('dogApi/',dogApi,name="dogApi"),
    path('login/',login,name="login"),
    path('noCuenta/',noCuenta,name="noCuenta"),
    path ('mostrar/', mostrar, name="mostrar"),
    path ('form_producto/', form_producto, name="form_producto"),
    path ('form_mod_producto/<id>', form_mod_producto, name="form_mod_producto"),
    path ('form_del_producto/<id>', form_del_producto, name="form_del_producto"),
    path ('mostrar_clientes/', mostrar1, name="mostrar_clientes"),
    path ('form_clientes/', form_clientes, name="form_clientes"),
    path ('form_mod_clientes/<id>', form_mod_clientes, name="form_mod_clientes"),
    path ('form_del_clientes/<id>', form_del_clientes, name="form_del_clientes"),
    path ('registrar/',registrar, name="registrar"),
    path ('detail/<slug>',detail, name="detail"),
    path ('<slug>/cart',cart, name="cart"),
    path ('mycart/',mycart, name="mycart"),
    path ('pedido/',pedido, name="pedido"),
    path ('exitosa/',exitosa,name="exitosa"),
    

]