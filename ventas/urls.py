from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views.venta_views import VentaViewSet

router = DefaultRouter()
router.register(r'veentas', VentaViewSet)  # Registra el viewset en la ruta 'ventas'

urlpatterns = [
    path('', include(router.urls)),
]