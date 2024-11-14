from django.contrib import admin
from django.urls import path, reverse
from django.shortcuts import redirect
from django.utils.html import format_html
from mesas.models import Mesa

@admin.register(Mesa)
class MesaAdmin(admin.ModelAdmin):
    list_display = ['numero', 'capacidad', 'estado', 'asignado_a', 'agregar_productos_link']
    list_filter = ['estado', 'asignado_a']
    search_fields = ['numero']
    ordering = ['estado', 'numero']
    list_per_page = 20

    fieldsets = (
        (None, {
            'fields': ('numero', 'capacidad', 'estado', 'asignado_a')
        }),
    )
    
    # Método para crear el enlace "Agregar productos" en la vista de detalles
    def agregar_productos_link(self, obj):
        url = reverse('admin:agregar_producto_mesa', args=[obj.id])
        return format_html('<a class="button" href="{}">Agregar productos</a>', url)
    agregar_productos_link.short_description = 'Agregar productos'

    # URL personalizada para manejar la vista de agregar productos
    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path(
                '<int:mesa_id>/agregar-producto/',
                self.admin_site.admin_view(self.agregar_productos_view),
                name='agregar_producto_mesa',
            ),
        ]
        return custom_urls + urls

    # Vista para el enlace "Agregar productos"
    def agregar_productos_view(self, request, mesa_id):
        # Aquí puedes implementar la lógica para agregar productos a la mesa
        self.message_user(request, f'Función agregar productos en mesa {mesa_id} no implementada aún.')
        return redirect(f"/admin/mesas/mesa/{mesa_id}/change/")