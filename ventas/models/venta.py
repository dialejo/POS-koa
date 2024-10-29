from django.db import models
from django.conf import settings
from mesas.models.mesa import Mesa
from productos.models.producto import Producto

class Venta(models.Model):
    mesa = models.ForeignKey(Mesa,on_delete=models.CASCADE)
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE,related_name='ventas')
    
    cantidad = models.PositiveSmallIntegerField()
    total = models.DecimalField(max_digits=100,decimal_places=3)
    fecha = models.DateField(auto_now_add=True)
    
    def __str__(self):
         return f'Venta {self.id} - Mesa {self.mesa.numero}'