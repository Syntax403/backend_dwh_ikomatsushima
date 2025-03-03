from rest_framework.generics import CreateAPIView
from django.contrib.auth import get_user_model
from .serializers import RegisterSerializer
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from .permissions import IsEditor, IsPeriodista, IsGestorActividades, IsFotografo
User = get_user_model()

class RegisterUserView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]


class OnlyPeriodistasView(APIView):
    permission_classes = [IsPeriodista]

    def get(self, request):
        return Response({"message": "Solo los periodistas pueden ver esto."})

class OnlyGestoresActividadesView(APIView):
    permission_classes = [IsGestorActividades]

    def get(self, request):
        return Response({"message": "Solo los gestores de actividades pueden ver esto."})

class OnlyFotografosView(APIView):
    permission_classes = [IsFotografo]

    def get(self, request):
        return Response({"message": "Solo los fotógrafos pueden ver esto."})