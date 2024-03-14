from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework_jwt.settings import api_settings
from django.contrib.auth import get_user_model, authenticate, login, logout

from .serializers import UserSerializer

User = get_user_model()


@api_view(['POST'])
@permission_classes([AllowAny])
def register_view(request):
    """
    Регистрация нового пользователя.
    """
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([AllowAny])
def login_view(request):
    """
    Вход пользователя в систему и выдача JWT токена, сохраняемого в cookie.
    """
    username = request.data.get('username')
    password = request.data.get('password')

    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)
        response = Response()
        response.set_cookie(key='jwt', value=token, httponly=True)
        return response
    else:
        return Response({'error': 'Неверный логин или пароль!'}, status=400)


@api_view(['POST'])
def logout_view(request):
    """
    Выход пользователя из системы и удаление JWT токена.
    """
    logout(request)
    response = Response()
    response.delete_cookie('jwt')
    return response
