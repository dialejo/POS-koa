from django.db import models
from django.conf import settings
from mesas.models.mesa import Mesa
from productos.models.producto import Producto
from ventas.models.venta_producto import VentaProducto
from decimal import Decimal

class Venta(models.Model):
    ESTADOS = [
        ('abierta','Abierta'),
        ('cerrada','Cerrada'),
    ]
    SERVICIO_PORCENTAJE = 0.10  # Inicialmente 10%
    
    mesa = models.ForeignKey(Mesa,on_delete=models.CASCADE)
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=10, choices=ESTADOS, default='cerrada')
    total = models.DecimalField(max_digits=100, decimal_places=3, blank=True, null= True)
    total_con_servicio = models.DecimalField(max_digits=100, decimal_places=3, blank=True, null=True)
    
    productos = models.ManyToManyField(Producto, through='DetalleVenta')
    
    def agregar_producto(self, producto, cantidad):
        """Agrega un producto a la venta si la mesa está ocupada"""
        detalle_venta = DetalleVenta(venta = self,producto=producto,cantidad=cantidad)
        detalle_venta.save()

    def actualizar_totales(self):
        """Actualiza el total y el total con servicio basado en los productos agregados"""
        total = sum(item.subtotal() for item in self.ventaproducto_set.all())
        self.total = total
        self.total_con_servicio = total * Decimal(1 + Venta.SERVICIO_PORCENTAJE)
        self.save(update_fields=['total', 'total_con_servicio'])
        
    def cerrar_venta(self):
        """Cierra la venta, calculando el total si aún no se ha calculado."""
        # Si la venta no tiene total calculado, lo hace ahora.
        if self.total is None or self.total_con_servicio is None:
            self.actualizar_totales() 
        self.estado = 'cerrada' 
        self.save() 
        
        for item in self.ventaproducto_set.all():
            item.producto.actualizar_inventario(item.cantidad)
class DetalleVenta(models.Model):
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    def __str__(self):
         return f'Venta {self.id} - Mesa {self.mesa.numero}'