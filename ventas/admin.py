from django.contrib import admin
from .models.venta import Venta
# Register your models here.

@admin.register(Venta)
class VentaAdmin(admin.ModelAdmin):
    list_display = ('id', 'mesa', 'fecha', 'total', 'usuario')  
    search_fields = ('mesa__numero', 'usuario__username')
    list_filter = ('fecha',)
    ordering = ('-fecha',)

    def total(self, obj):
        return sum(producto.precio for producto in obj.productos.all())