from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import News
from .serializers import NewsSerializer

class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = [IsAuthenticated]  # Solo usuarios autenticados pueden acceder

    def perform_create(self, serializer):
        """
        Antes de crear una noticia, aseguramos que el usuario sea Admin o periodista.
        """
        user = self.request.user
        if user.role != 'admin' and user.sub_role != 'periodista':
            return Response(
                {"error": "Solo los administradores y periodistas pueden crear noticias."},
                status=status.HTTP_403_FORBIDDEN
            )
        serializer.save(autor=user)
