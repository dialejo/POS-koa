from rest_framework import serializers
from ..models.venta import Venta 
from productos.serializers.producto_serializers import ProductoSerializer
from productos.models.producto import Producto
from ventas.models.venta_producto import VentaProducto

class VentaProductoSerializer(serializers.ModelSerializer):
    
    subtotal = serializers.SerializerMethodField()
    """Serializer para la relación entre Venta y Producto"""
    class Meta:
        model = VentaProducto
        fields = ['producto', 'cantidad', 'subtotal']  # Subtotal lo calculamos en el modelo

class VentaSerializer(serializers.ModelSerializer):
    """Serializer para la venta"""
    productos = VentaProductoSerializer(many=True, read_only=True)  # Muestra los productos de la venta
    total = serializers.DecimalField(max_digits=100, decimal_places=3, read_only=True)
    total_con_servicio = serializers.DecimalField(max_digits=100, decimal_places=3, read_only=True)
    
    class Meta:
        model = Venta
        fields = ['id', 'mesa', 'usuario', 'fecha', 'estado', 'total', 'total_con_servicio', 'productos']
        read_only_fields = ['estado', 'total', 'total_con_servicio']

    def create(self, validated_data):
        """
        Sobrescribimos el método `create` para agregar la lógica al momento de crear una venta.
        Esta lógica está asociada a la mesa y al estado de la venta.
        """
        productos_data = self.context['request'].data.get('productos', [])
        
        venta = Venta.objects.create(**validated_data)
        
        # Agregar los productos a la venta en el momento de la creación
        for producto_data in productos_data:
            producto = Producto.objects.get(id=producto_data['producto'])
            cantidad = producto_data['cantidad']
            VentaProducto.objects.create(venta=venta, producto=producto, cantidad=cantidad)
        
        return venta

    def update(self, instance, validated_data):
        """Actualizar los datos de la venta, incluyendo los productos si es necesario"""
        # Se actualizan los productos en la venta si se pasan nuevos datos.
        productos_data = self.context['request'].data.get('productos', [])
        
        # Actualizamos los campos normales de la venta
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        
        # Actualizar los productos asociados si es necesario
        if productos_data:
            for producto_data in productos_data:
                producto = Producto.objects.get(id=producto_data['producto'])
                cantidad = producto_data['cantidad']
                
                # Verificamos si el producto ya está en la venta
                venta_producto = VentaProducto.objects.filter(venta=instance, producto=producto).first()
                if venta_producto:
                    venta_producto.cantidad = cantidad
                    venta_producto.save()
                else:
                    # Si no está, lo agregamos
                    VentaProducto.objects.create(venta=instance, producto=producto, cantidad=cantidad)
        
        # Guardar la venta actualizada
        instance.save()
        
        return instance