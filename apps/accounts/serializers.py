from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'role', 'sub_role']
        extra_kwargs = {'password': {'write_only': True}}

    def validate(self, data):
        """
        Valida que solo los editores puedan tener un sub-role.
        """
        if data.get('role') != 'editor' and data.get('sub_role'):
            raise serializers.ValidationError("Solo los editores pueden tener un sub-rol.")

        # Validar que si el rol es editor, el sub-role sea válido
        valid_sub_roles = ['periodista', 'gestor_actividades', 'fotografo']
        if data.get('role') == 'editor' and data.get('sub_role') not in valid_sub_roles:
            raise serializers.ValidationError("El sub-rol asignado no es válido para editores.")

        return data

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
