from django.db import models
from django.conf import settings

class Mesa(models.Model):
    ESTADOS = [ 
                ('disponible','Disponible'),
                ('ocupada', 'Ocupada')
                ]
    numero = models.CharField('numero o nombre de mesa', max_length =10, unique = True)
    capacidad = models.PositiveIntegerField('Capacidad')
    estado = models.CharField('Estado', max_length=10, choices=ESTADOS, default='disponible')
    asignado_a = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.SET_NULL,
        null=True, 
        blank=True,
        related_name='mesas_asignadas'
    )
    
    def __str__(self):
        return f'Mesa {self.numero} - {self.get_estado_display()}'
               
   
    