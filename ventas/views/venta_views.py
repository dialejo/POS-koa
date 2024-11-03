from rest_framework import viewsets
from ..serializers.venta_serializers import VentaSerializer
from ..models.venta import Venta
from productos.models.producto import Producto

class VentaViewSet(viewsets.ModelViewSet):
    queryset = Venta.objects.all()
    serializer_class = VentaSerializer
    
    def perform_create(self, serializer):
        total = self.calculate_total(serializer.validated_data.get('productos', []))
        serializer.save(total=total)
        
    def calculate_total(self, productos_data):
        total = 0
        for producto_data in productos_data:
            producto_id = producto_data.get('id')  
            cantidad = producto_data.get('cantidad', 1)  
            try:
                producto = Producto.objects.get(id=producto_id)
                total += producto.precio * cantidad
            except Producto.DoesNotExist:
                continue 
        return total
