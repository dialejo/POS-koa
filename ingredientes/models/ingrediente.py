from django.db import models

class ingrediente(models.Model):
    UNIDADES_CHOICES = [
        ('kg','kilogramos'),
        ('L','litros'),
        ('oz','Onzas'),
        ('U','unidad'),
    ]
    
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=3)
    unidad = models.CharField(max_length=10, choices=UNIDADES_CHOICES)
    
    def __str__(self):
        return f"{self.nombre} - {self.unidad}"