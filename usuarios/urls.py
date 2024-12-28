from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views.user_views import UserViewSet
from .views import UserViewSet, RegisterView

router = DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('usuarios/register/', RegisterView.as_view(), name='register'),
]