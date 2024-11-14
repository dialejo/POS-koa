from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views.venta_views import VentaCreateView, VentaAgregarProductoView, VentaCerrarView, VentaCancelarProductoView

urlpatterns = [
    path('venta/', VentaCreateView.as_view(), name='crear-venta'),
    path('venta/agregar-producto/', VentaAgregarProductoView.as_view(), name='agregar-producto'),
    path('venta/cerrar/', VentaCerrarView.as_view(), name='cerrar-venta'),
    path('venta/cancelar-producto/', VentaCancelarProductoView.as_view(), name='cancelar-producto'),
]
