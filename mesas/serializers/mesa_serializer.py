from rest_framework import serializers
from mesas.models import Mesa

class MesaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mesa
        fields = ['id', 'numero', 'capacidad', 'estado', 'asignado_a']