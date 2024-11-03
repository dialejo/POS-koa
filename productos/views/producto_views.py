from rest_framework import viewsets
from ..models import Producto, Categoria  # Importamos los modelos Producto y Categoria
from ..serializers.producto_serializers import ProductoSerializer, CategoriaSerializer  # Importamos los serializers

class CategoriaViewSet(viewsets.ModelViewSet):
    """
    Vista para gestionar las categorías de productos.
    """
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class ProductoViewSet(viewsets.ModelViewSet):
    """
    Vista para gestionar los productos, con operaciones CRUD.
    """
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer