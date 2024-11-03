from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from ..models import Ingrediente
from ..serializers.ingrediente_serializer import IngredienteSerializer

class IngredienteViewSet(viewsets.ModelViewSet):
    queryset = Ingrediente.objects.all()
    serializer_class = IngredienteSerializer
    permission_classes = [IsAuthenticated]