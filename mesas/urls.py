from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MesaViewSet
from .views.mesa_view import AbrirMesaView, CerrarMesaView, AgregarProductoAMesaView

router = DefaultRouter()
router.register(r'mesas', MesaViewSet)

urlpatterns = [
    path('api/', include(router.urls)),  # CRUD de mesas
    path('mesas/<int:mesa_id>/abrir/', AbrirMesaView.as_view(), name='abrir_mesa'),
    path('mesas/<int:mesa_id>/cerrar/', CerrarMesaView.as_view(), name='cerrar_mesa'),
    path('mesas/<int:mesa_id>/agregar-producto/', AgregarProductoAMesaView.as_view(), name='agregar_producto_mesa'),
] 
