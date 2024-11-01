from django.db import models
from django.conf import settings
from mesas.models.mesa import Mesa
from productos.models.producto import Producto
from decimal import Decimal

class Venta(models.Model):
    SERVICIO_PORCENTAJE = 0.10  # Inicialmente 10%
    
    mesa = models.ForeignKey(Mesa,on_delete=models.CASCADE)
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE,related_name='ventas')
    cantidad = models.PositiveSmallIntegerField()
    total = models.DecimalField(max_digits=100, decimal_places=3, blank=True, null= True)
    total_con_servicio = models.DecimalField(max_digits=100, decimal_places=3, blank=True, null=True)
    
    def save(self,*args, **kwargs):
        if not self.total:
            self.total = Decimal(self.producto.precio) * Decimal(self.cantidad)
        
        self.total_con_servicio = self.total * Decimal(1 + Venta.SERVICIO_PORCENTAJE)
        
        super().save(*args, **kwargs)
    
    @classmethod
    def set_servicio_porcentaje(cls, nuevo_porcentaje):
        """Método de clase para actualizar el porcentaje de servicio"""
        cls.SERVICIO_PORCENTAJE = nuevo_porcentaje
        
    def __str__(self):
         return f'Venta {self.id} - Mesa {self.mesa.numero}'