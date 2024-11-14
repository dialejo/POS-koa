from django.db import models
from django.conf import settings
from django.apps import apps

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
    
    
    def abrir(self, usuario):
        if self.estado == 'ocupada':
            raise ValueError("La mesa ya está ocupada.")
        self.estado = 'ocupado'
        self.asignado_a = usuario
        self.save()
        
        # Usar get_model para acceder al modelo Venta sin hacer importación circular
        Venta = apps.get_model('ventas', 'Venta')  # Accedemos al modelo Venta usando get_model
        venta = Venta.objects.create(mesa=self, usuario=usuario, estado='abierta')
        return venta
        
    def cerrar(self):
        if self.estado == 'disponible':
            raise ValueError("La mesa ya está disponible")
        self.estado = 'disponible'
        self.asignado_a = None
        self.save()
        
        
        # Cerrar la venta asociada
        Venta = apps.get_model('ventas', 'Venta')  # Usar get_model para evitar import circular
        venta_abierta = Venta.objects.filter(mesa=self, estado='abierta').first()
        if venta_abierta:
            venta_abierta.cerrar_venta()
        
        
    def agregar_producto(self, producto, cantidad):
        if self.estado != 'ocupado':
            raise ValueError("No se pueden agregar productos a una mesa no ocupada.")
        
        # Usar get_model para acceder al modelo Venta sin hacer importación circular
        Venta = apps.get_model('ventas', 'Venta')  # Accedemos al modelo Venta usando get_model
        venta = Venta.objects.filter(mesa=self, estado='abierta').first()
        if not venta:
            venta = self.abrir(self.asignado_a)
        
        venta.agregar_producto(producto, cantidad)

        
    def __str__(self):
        return f'Mesa {self.numero} - {self.get_estado_display()}'
        
        
               
   
    