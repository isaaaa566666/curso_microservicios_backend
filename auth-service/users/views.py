from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

User = get_user_model()

@api_view(['POST'])
def register_user(request):
    """
    Registrar usuario usando el AUTH_USER_MODEL (acepta 'email' y 'password').
    """
    email = request.data.get('email')
    password = request.data.get('password')

    if not email or not password:
        return Response({'error': 'Email y password son obligatorios'}, status=status.HTTP_400_BAD_REQUEST)

    if User.objects.filter(email=email).exists():
        return Response({'error': 'El usuario ya existe'}, status=status.HTTP_400_BAD_REQUEST)

    user = User.objects.create_user(email=email, password=password)

    return Response({'message': 'Usuario creado exitosamente', 'id': user.id}, status=status.HTTP_201_CREATED)