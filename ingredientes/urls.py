from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views.ingrediente_views import IngredienteViewSet

router = DefaultRouter()
router.register(r'ingredientes', IngredienteViewSet)

urlpatterns = [
    path('', include(router.urls)),
]