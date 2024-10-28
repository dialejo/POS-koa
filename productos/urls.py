from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views.producto_views import ProductoViewSet, CategoriaViewSet

# Creamos un router y registramos nuestros viewsets
router = DefaultRouter()
router.register(r'productos', ProductoViewSet)
router.register(r'categorias', CategoriaViewSet)

urlpatterns = [
    path('', include(router.urls)),  # Incluimos las rutas generadas por el router
]