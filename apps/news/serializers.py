from rest_framework import serializers
from .models import News

class NewsSerializer(serializers.ModelSerializer):
    autor = serializers.StringRelatedField()  # Muestra el nombre del autor en lugar del ID

    class Meta:
        model = News
        fields = '__all__'

    def validate_autor(self, value):
        """
        Asegura que solo un Admin o un Fotógrafo puede ser autor de la noticia.
        """
        if value.role != 'admin' and value.sub_role != 'periodista':
            raise serializers.ValidationError("Solo los administradores y periodistas pueden ser autores.")
        return value
