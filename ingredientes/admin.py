from django.contrib import admin
from .models.ingrediente import Ingrediente
from productos.models.producto import Producto
# Register your models here.

@admin.register(Ingrediente)
class IngredienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'unidad')
    search_fields = ('nombre',)
    list_filter = ('unidad',)
