# django-jwt-cookie-auth

Аутентификация с использованием JWT токенов, хранящиеся в cookie для безопасной передачи и хранения на стороне клиента.

## Установка зависимостей

Для установки зависимостей выполните следующую команду:

```
pip install -r requirements.txt
```

## Применение миграций

Для применения миграций выполните следующие команды:

```
python manage.py makemigrations
python manage.py migrate
```

## Эндпойнты

### Регистрация нового пользователя

POST `/auth/signup/`

Пример запроса:

```
{
    "username": "example_user",
    "password": "example_password",
    "email": "example@example.com"
}
```

### Аутентификация пользователя

POST `/auth/login/`

Пример запроса:

```
{
    "username": "example_user",
    "password": "example_password"
}
```

### Выход пользователя

POST `/api/logout/`

###