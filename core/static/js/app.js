//Validacion Contacto
$(function() 
{
  $("#formContacto").validate({
       rules: {                   
              nom:"required",
              ema:{
                  required:true,
                  email: true
              },
              asu:"required",
              tA:"required", 
          }, //rules
      messages:{
          nom: {
              required:'Ingresa un nombre',
              minlength:'Cantidad de caracteres insuficiente'
          },
          ema: {
              required:'Ingresa tu correo electrónico',
              email:'Formato de correo no válido'
          },
          asu:{
              required:'Ingrese minimo 5 caracteres',
              minlength:'Cantidad de caracteres insuficiente'
          },
          tA:{
              required:'Ingrese un mensaje',
          }
        }
    }); 
}); 
//validacion

$(function() 
{
  $("#formRegistrar").validate({
       rules: {
            nombre:"required",
            apellido:"required",
            numero:"required",
            email:{
                required:true,
                email:true
            },
            contra:"required",
            },   
            contra2: {
                required: true,
                equalTo:"#contra"
            }  ,
              
           //rules
      messages: {
        nombre:{
            required:'Ingrese Nombre',
            minlength:'Cantidad de caracteres insuficiente'
          },
        apellido:{
            required:'Ingrese Apellido',
          },
        numero:{
            required: 'Ingrese un número de celular',
            minlength: 'Cantidad de digitos insuficiente'
          },
        email: {
            required: 'Ingresa tu correo electrónico',
            email: 'Formato de correo no válido'
          },
        contra: {
            required: 'Ingresa una contraseña',
            minlength: 'Caracteres insuficientes'

        },
        contra2: {
            required: 'Reingresa la contraseña',
            equalTo: 'Las contraseñas ingresadas no coinciden',
            minlength: 'Caracteres insuficientes'
      }
    }
  }); 
}); 
 
function CambiaColor(a)
        {
            a.style.background = "orange";
        }
function CambiarMayusculas(){
    var a = document.getElementById('nom');
    a.value = a.value.toUpperCase();
}

function cambiarImg1() {
    
    document.getElementById("Img11").src = "{% static 'img/lobo.jpg' %}";
       }
function cambiarImg2(){
    document.getElementById("Img11").src = "{% static 'img/productos.png' %}";
       }    

//RELOJ
function actual() {
fecha=new Date(); //Actualizar fecha.
hora=fecha.getHours(); //hora actual
minuto=fecha.getMinutes(); //minuto actual
segundo=fecha.getSeconds(); //segundo actual
if (hora<10) { //dos cifras para la hora
    hora="0"+hora;
    }
if (minuto<10) { //dos cifras para el minuto
    minuto="0"+minuto;
    }
if (segundo<10) { //dos cifras para el segundo
    segundo="0"+segundo;
    }
//ver en el recuadro del reloj:
mireloj = hora+" : "+minuto+" : "+segundo;	
        return mireloj; 
}
function actualizar() { //función del temporizador
  mihora=actual(); //recoger hora actual
  mireloj=document.getElementById("reloj"); //buscar elemento reloj
  mireloj.innerHTML=mihora; //incluir hora en elemento
    }
setInterval(actualizar,1000); //iniciar temporizador

//PERROSAPI
$(document).ready(function(){

    $('.animalCliente').click(function(){
            $("#categorias").empty();
            $.getJSON("https://dog.ceo/api/breeds/image/random/3", function( data ) {
                $("#perros").html(JSON.stringify(data, null, 4));//Para que no se multipiqle
        
                $.each(data.message, function(index, item) {
                    $("#categorias").append("<tr><td>"+ "</td><td><img src='"+ item +"'>"
                    +"</td></tr>");
                });
            });
        
    
    
    });
    
    });
//MAPA CON GOOGLE
function iniciarMap(){
    var coord = {lat:-33.5162213 ,lng: -70.7525726};
    var map = new google.maps.Map(document.getElementById('map'),{
      zoom: 10,
      center: coord
    });
    var marker = new google.maps.Marker({
      position: coord,
      map: map
    });
}

$(function(){
    $("#validacion").validate({
          rules: {
                id_producto : "required",
                descripcionP: "required",
                marca: "required",
                imagen: "required",
                categoria :"required",
                },   
            messages: 
            {
            id_producto: {
                required: 'Ingresa el id del producto',
              },
            descripcionP: {
                required: 'Ingresa descripcion',
                maxlenght:'No ingresar más de 60 caracteres'
            },
            marca:{
                required: 'Ingrese marca',  
            },
            imagen:{
                required: 'Ingrese imagen',  
            },
            categoria:{
                required: 'Seleccione una categoria',
            },
              
        }
    }); 
  });

  $(function(){
    $("#validacionA").validate({
          rules: {
                rut_cliente : "required",
                nombres_clientes: "required",
                apellidos_clientes: "required",
                correos_clientes: "required",
                dirreciones_clientes :"required",
                num_cel_clientes:"required", 
                sexo :"required",
                },   
            messages: 
            {
                rut_cliente: {
                required: 'Ingrese rut de cliente ',
              },
              nombres_clientes: {
                required: 'Ingrese nombre de cliente',
                maxlenght:'No ingresar más de 60 caracteres'
            },
            apellidos_clientes:{
                required: 'Ingrese apellido cliente',  
            },
            correos_clientesn:{
                required: 'Ingrese correo',  
            },
            dirreciones_clientes:{
                required: 'Ingrese direccion',
            },
            num_cel_clientes:{
                required: 'Ingrese numero de telefono',
            },
            sexo:{
                required: 'Ingrese su sexo',
            },
              
        }
    }); 
  });