from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=100,unique=True)
    
    def __str__(self):
        return self.nombre
    
class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True, null=True)
    costo = models.DecimalField(max_digits=10, decimal_places=3)
    precio = models.DecimalField(max_digits=10,decimal_places=3)
    stock = models.PositiveBigIntegerField()
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, related_name='productos')
    
    def __str__(self):
        return self.nombre
    