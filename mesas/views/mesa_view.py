from rest_framework import viewsets
from mesas.models import Mesa
from mesas.serializers import MesaSerializer

class MesaViewSet(viewsets.ModelViewSet):
    queryset = Mesa.objects.all()
    serializer_class = MesaSerializer

    def get_queryset(self):
        if self.request.user.is_staff:
            return Mesa.objects.all()
        return Mesa.objects.filter(asignado_a=self.request.user)