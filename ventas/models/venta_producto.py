from django.db import models
from productos.models.producto import Producto
from django.apps import apps

class VentaProducto(models.Model):
    venta = models.ForeignKey('ventas.Venta', on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()

    def subtotal(self):
        return self.producto.precio * self.cantidad
    
    def save(self, *args, **kwargs):
        # Accedemos al modelo Venta con apps.get_model
        Venta = apps.get_model('ventas', 'Venta')
        # Aquí puedes agregar la lógica adicional si es necesario
        super().save(*args, **kwargs)

    def __str__(self):
        return f"VentaProducto {self.venta.id} - {self.producto.nombre}"