from rest_framework import serializers
from ..models import Producto, Categoria


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ['id', 'nombre']  # Los campos que queremos exponer

class ProductoSerializer(serializers.ModelSerializer):
    # Mostrar el nombre de la categoría en lugar de solo el ID
    categoria = serializers.StringRelatedField()  

    class Meta:
        model = Producto
        fields = ['id', 'nombre', 'descripcion', 'precio', 'stock', 'categoria']