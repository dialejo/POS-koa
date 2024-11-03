from rest_framework import serializers
from ..models import Producto, Categoria
from ..models.ingrediente_producto import IngredienteProducto
from ingredientes.serializers.ingrediente_serializer import IngredienteSerializer


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ['id', 'nombre']  # Los campos que queremos exponer
        
class IngredienteProductoSerializer(serializers.ModelSerializer):
    ingrediente = IngredienteSerializer()
    
    class Meta:
        model = IngredienteProducto
        fields = ['ingrediente', 'cantidad']
        

class ProductoSerializer(serializers.ModelSerializer):
    # Mostrar el nombre de la categoría en lugar de solo el ID
    categoria = serializers.StringRelatedField()  
    ingredientes = IngredienteProductoSerializer(source='ingredientes_producto', many=True)

    class Meta:
        model = Producto
        fields = ['id', 'nombre', 'descripcion','costo' ,'precio', 'stock', 'categoria','ingredientes']