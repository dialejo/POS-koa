from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from mesas.models import Mesa
from productos.models.producto import Producto
from mesas.serializers import MesaSerializer

class MesaViewSet(viewsets.ModelViewSet):
    queryset = Mesa.objects.all()
    serializer_class = MesaSerializer

class AbrirMesaView(APIView):
    
    def post(self, request, mesa_id):
        try:
            mesa = Mesa.objects.get(id=mesa_id)
            venta = mesa.abrir(request.user)  # Abrir la mesa y crear una venta
            return Response({'message': f'Mesa {mesa.numero} abierta y venta {venta.id} creada.'}, status=status.HTTP_200_OK)
        except Mesa.DoesNotExist:
            return Response({'error': 'Mesa no encontrada.'}, status=status.HTTP_404_NOT_FOUND)
        except ValueError as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

class CerrarMesaView(APIView):
    
    def post(self, request, mesa_id):
        try:
            mesa = Mesa.objects.get(id=mesa_id)
            mesa.cerrar()  # Cerrar la mesa
            return Response({'message': f'Mesa {mesa.numero} cerrada.'}, status=status.HTTP_200_OK)
        except Mesa.DoesNotExist:
            return Response({'error': 'Mesa no encontrada.'}, status=status.HTTP_404_NOT_FOUND)
        except ValueError as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

class AgregarProductoAMesaView(APIView):
    
    def post(self, request, mesa_id):
        try:
            mesa = Mesa.objects.get(id=mesa_id)
            producto_id = request.data.get('producto_id')
            cantidad = request.data.get('cantidad')
            
            # Obtener el producto de la base de datos
            producto = Producto.objects.get(id=producto_id)
            
            # Agregar el producto a la venta de la mesa
            mesa.agregar_producto(producto, cantidad)
            
            return Response({'message': f'Producto {producto.nombre} agregado a la mesa {mesa.numero}.'}, status=status.HTTP_200_OK)
        except Mesa.DoesNotExist:
            return Response({'error': 'Mesa no encontrada.'}, status=status.HTTP_404_NOT_FOUND)
        except Producto.DoesNotExist:
            return Response({'error': 'Producto no encontrado.'}, status=status.HTTP_404_NOT_FOUND)
        except ValueError as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)