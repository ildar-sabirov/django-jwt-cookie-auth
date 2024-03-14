from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели пользователя.

    Поля:
    - id: ID пользователя (только для чтения)
    - username: Имя пользователя
    - password: Пароль пользователя (только для записи)
    - email: Электронная почта пользователя
    - first_name: Имя пользователя
    - last_name: Фамилия пользователя

    Методы:
    - create: Создает и возвращает нового пользователя.
    """
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'password',
            'email',
            'first_name',
            'last_name'
        )

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
