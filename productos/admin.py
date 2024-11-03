from django.contrib import admin
from .models import Categoria, Producto
from .models.ingrediente_producto import IngredienteProducto


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)  # Muestra el nombre de la categoría en la lista
    search_fields = ('nombre',)  # Permite buscar por nombre
    
class IngredienteProductoInline(admin.TabularInline):
    model = IngredienteProducto
    extra = 1 

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    inlines = [IngredienteProductoInline]
    list_display = ('nombre', 'precio', 'stock', 'categoria','costo_total')  # Campos a mostrar en la lista
    list_filter = ('categoria',)  # Permite filtrar por categoría
    search_fields = ('nombre',)  # Permite buscar por nombre
    
    def costo_total(self, obj):
        return obj.costo_total()
    costo_total.short_description = 'Costo Total'