# django-jwt-cookie-auth

Аутентификация с использованием JSON Web Token, хранящихся в cookie для безопасной передачи и хранения на стороне клиента.

## Клонирование проекта

Выполните команду:

```
git clone git@github.com:ildar-sabirov/django-jwt-cookie-auth.git
```

## Установка зависимостей

Выполните команду:

```
pip install -r requirements.txt
```

## Применение миграций

Выполните команду:

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