from rest_framework import serializers
from core.models import Clientes

class ClientesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Clientes
        fields = ['rut_cliente', 'nombres_cliente', 'apellidos_clientes', 'correos_clientes','dirreciones_clientes','num_cel_clientes','sexo']