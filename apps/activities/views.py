from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import Activity
from .serializers import ActivitySerializer

class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer
    permission_classes = [IsAuthenticated]  # Solo usuarios autenticados

    def perform_create(self, serializer):
        """Asegura que el usuario sea Admin o Gestor de Actividades antes de crear la actividad."""
        user = self.request.user
        if user.role != 'admin' and user.sub_role != 'gestor_actividades':
            return Response(
                {"error": "Solo los administradores y gestores de actividades pueden crear actividades."},
                status=status.HTTP_403_FORBIDDEN
            )
        serializer.save(autor=user)
