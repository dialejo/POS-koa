from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..serializers.venta_serializers import VentaSerializer
from ..models.venta import Venta
from productos.models.producto import Producto
from ..models.venta_producto import VentaProducto
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.shortcuts import get_object_or_404

class VentaCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        """Crear una nueva venta asociada a una mesa."""
        mesa_id = request.data.get('mesa_id')
        mesa = get_object_or_404(mesa, id=mesa_id)
        
        # Verificamos si la mesa está disponible para ser ocupada
        if mesa.estado != 'disponible':
            return Response({"detail": "La mesa no está disponible."}, status=status.HTTP_400_BAD_REQUEST)
        
        # Crear la venta
        venta = mesa.abrir(request.user)
        
        # Serializar la venta creada
        serializer = VentaSerializer(venta)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class VentaAgregarProductoView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        """Agregar productos a una venta abierta."""
        venta_id = request.data.get('venta_id')
        producto_id = request.data.get('producto_id')
        cantidad = request.data.get('cantidad')
        
        venta = get_object_or_404(Venta, id=venta_id, estado='abierta')
        producto = get_object_or_404(Producto, id=producto_id)
        
        # Agregar producto a la venta
        try:
            venta.agregar_producto(producto, cantidad)
        except ValueError as e:
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
        return Response({"detail": "Producto agregado correctamente."}, status=status.HTTP_200_OK)


class VentaCancelarProductoView(APIView):
    """Vista para cancelar (eliminar) un producto de una venta, solo accesible para administradores"""
    permission_classes = [IsAdminUser]  # Solo administradores pueden cancelar productos

    def post(self, request, *args, **kwargs):
        """Cancelar (eliminar) un producto de la venta."""
        venta_id = request.data.get('venta_id')
        producto_id = request.data.get('producto_id')
        
        venta = get_object_or_404(Venta, id=venta_id, estado='abierta')  # Solo en ventas abiertas
        producto = get_object_or_404(Producto, id=producto_id)
        
        # Verificamos si el producto está en la venta
        venta_producto = VentaProducto.objects.filter(venta=venta, producto=producto).first()
        if not venta_producto:
            return Response({"detail": "El producto no está en esta venta."}, status=status.HTTP_400_BAD_REQUEST)
        
        # Eliminar el producto de la venta
        venta_producto.delete()
        
        # Actualizar totales después de la eliminación
        venta.actualizar_totales()
        
        return Response({"detail": "Producto cancelado correctamente."}, status=status.HTTP_200_OK)


class VentaCerrarView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        """Cerrar una venta y calcular los totales."""
        venta_id = request.data.get('venta_id')
        venta = get_object_or_404(Venta, id=venta_id)
        
        # Cerrar la venta
        venta.cerrar_venta()
        
        return Response({"detail": "Venta cerrada correctamente."}, status=status.HTTP_200_OK)
