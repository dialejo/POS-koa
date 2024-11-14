from rest_framework import serializers
from mesas.models.mesa import Mesa
from ventas.models.venta import Venta

class MesaSerializer(serializers.ModelSerializer):
    # Si deseas incluir la información de la venta asociada a la mesa
    venta = serializers.SerializerMethodField()

    class Meta:
        model = Mesa
        fields = ['id', 'numero', 'capacidad', 'estado', 'asignado_a', 'venta']
    
    def get_venta(self, obj):
        """Método para obtener la venta asociada a la mesa si está abierta"""
        venta_abierta = Venta.objects.filter(mesa=obj, estado='abierta').first()
        if venta_abierta:
            return {
                'id': venta_abierta.id,
                'total': str(venta_abierta.total),
                'total_con_servicio': str(venta_abierta.total_con_servicio),
                'fecha': venta_abierta.fecha,
                'estado': venta_abierta.get_estado_display()
            }
        return None