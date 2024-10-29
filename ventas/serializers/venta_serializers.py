from rest_framework import serializers
from ..models.venta import Venta 
from productos.serializers.producto_serializers import ProductoSerializer
from productos.models.producto import Producto

class VentaSerializer(serializers.ModelSerializer):
    producto = ProductoSerializer(many=True)
    
    class Meta:
        model = Venta
        fields ='__all__'
        
    def create(self, validated_data):
        productos_data = validated_data.pop('productos')
        venta = Venta.objects.create(**validated_data)
        
        for producto_data in productos_data:
            producto = Producto.objects.get(id=producto_data['id'])
            venta.productos.add(producto)
            
        return venta