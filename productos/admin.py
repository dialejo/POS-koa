from django.contrib import admin
from .models import Categoria, Producto

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)  # Muestra el nombre de la categoría en la lista
    search_fields = ('nombre',)  # Permite buscar por nombre

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'stock', 'categoria')  # Campos a mostrar en la lista
    list_filter = ('categoria',)  # Permite filtrar por categoría
    search_fields = ('nombre',)  # Permite buscar por nombre