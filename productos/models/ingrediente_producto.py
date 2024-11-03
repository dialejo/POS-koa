from django.db import models
from ingredientes.models import Ingrediente

class IngredienteProducto(models.Model):
    producto = models.ForeignKey('productos.Producto', on_delete=models.CASCADE, related_name='ingredientes') 
    ingrediente = models.ForeignKey(Ingrediente,on_delete=models.CASCADE)
    cantidad = models.DecimalField(max_digits=100,decimal_places=3)
    
    class Meta:
        unique_together = ('producto','ingrediente')
    
    def costo_total(self):
        return self.cantidad * self.ingrediente.precio

    def __str__(self):
        return f"{self.cantidad} {self.ingrediente.unidad} de {self.ingrediente.nombre}"
    