## О проекте:

Аутентификация с использованием JSON Web Token, хранящихся в cookie для безопасной передачи и хранения на стороне клиента.

## Технологии:

+ python 3.10
+ Django 3.2.16
+ djangorestframework 3.14.0
+ JSON Web Token Authentication
+ PostgreSQL
+ gunicorn
+ nginx
+ Docker

## Клонирование проекта

Выполните команду:

```
git clone git@github.com:ildar-sabirov/django-jwt-cookie-auth.git
```

## Настройка переменных среды

- Создайте файл .env в корневой директории проекта.

- Скопируйте содержимое файла .env.example в файл .env.

- Заполните переменные среды в файле .env в соответствии с вашей конфигурацией.

- Теперь то же самое проделываем для директории /backend

## Запуск проекта

Выполните команду:

```
docker-compose up
```

## Применение миграций и сбор статики

Выполните команды:

```
docker compose exec backend python manage.py migrate

docker compose exec backend python manage.py collectstatic
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

## Автор:
Ильдар Сабиров - [ildar-sabirov](https://github.com/ildar-sabirov)
