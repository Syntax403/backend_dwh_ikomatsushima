from rest_framework import serializers
from .models import Activity

class ActivitySerializer(serializers.ModelSerializer):
    autor = serializers.StringRelatedField()  # Muestra el nombre del autor en lugar del ID

    class Meta:
        model = Activity
        fields = '__all__'

    def validate_autor(self, value):
        """Valida que el autor sea un admin o un gestor de actividades."""
        if value.role != 'admin' and value.sub_role != 'gestor_actividades':
            raise serializers.ValidationError("Solo los administradores y gestores de actividades pueden crear actividades.")
        return value
