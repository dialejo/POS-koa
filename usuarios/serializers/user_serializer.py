from rest_framework import serializers
from ..models.user import User
from mesas.serializers.mesa_serializer import MesaSerializer

class UserSerializer(serializers.ModelSerializer):
    mesas_asignadas = MesaSerializer(many=True, read_only=True)
    nueva_contrasena = serializers.CharField(write_only=True, required=False) # nueva contraseña

    
    class Meta:
        model = User
        fields = ['id', 'username', 'name', 'email','password', 'mesas_asignadas','nueva_contrasena']
        extra_kwargs = {'password': {'write_only': True}}
        
        def create(self, validated_data): # super user es el unico que puede hacerle contraseñas a los usuarios
            nueva_contrasena = validated_data.pop('nueva_contrasena', None)
            user = super().create(validated_data)
            if nueva_contrasena:
                user.set_password(nueva_contrasena)  # Establece la nueva contraseña
                user.save()
                return user
        
        def update(self, instance, validated_data): # Si hay una nueva contraseña, se actualiza
            nueva_contrasena = validated_data.pop('nueva_contrasena', None)
            if nueva_contrasena:
                instance.set_password(nueva_contrasena)  # Actualiza la contraseña
                return super().update(instance, validated_data)