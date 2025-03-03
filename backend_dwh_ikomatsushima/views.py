from django.shortcuts import redirect
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from rest_framework import status

def home(request):
    return redirect('/admin/')  # Redirige automáticamente al panel de administración



class CustomTokenObtainPairView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        if response.status_code == 200:
            return Response({
                'token': response.data['access'],
                'refresh': response.data['refresh'],
                'message': 'Login exitoso'
            })
        return Response({'error': 'Credenciales inválidas'}, status=status.HTTP_401_UNAUTHORIZED)
