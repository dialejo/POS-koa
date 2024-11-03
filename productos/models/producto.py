from django.db import models
from ..models.ingrediente_producto import IngredienteProducto
from ingredientes.models.ingrediente import Ingrediente
from decimal import Decimal

class Categoria(models.Model):
    nombre = models.CharField(max_length=100,unique=True)
    
    def __str__(self):
        return self.nombre
    
class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True, null=True)
    costo = models.DecimalField(max_digits=10, decimal_places=2)
    precio = models.DecimalField(max_digits=10,decimal_places=2)
    stock = models.PositiveBigIntegerField()
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, related_name='productos')
    
    def costo_total(self):
        total = self.costo
        for ingrediente_producto in self.ingredientes.all():
            total += ingrediente_producto.costo_total()
        return total.quantize(Decimal('0.01'))
    
    def __str__(self):
        return self.nombre
    