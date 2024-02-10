# API

### Доступ к API
- Документация

    http://localhost:8000/api/redoc/ - Swagger
 
    http://localhost:8000/api/docs/ - Redoc
# Работа с пользователями
- Регистрация пользователей
    
    http://localhost:8000/api/auth/register/


- Запрос JSON на регистрацию
```
  {
    "email": "email",
    "first_name": "first_name",
    "last_name": "last_name",
    "password": "password"
  }
  ```
#### Валидация:

- Поле Email
- Пароль не менее 8 символов и не должен содержать только цифры

### Авторизация пользователей 

    http://localhost:8000/api/auth/login/

- Запрос JSON на авторизацию
```
{
    "email": "email",
    "password": "password"
}
```
#### Валидация:

- Поле Email

#### Ответ:
```
{
    "refresh": "REFRESH_TOKEN",
    "access": "ACCESS_TOKEN"
}
```


### Информация о пользовтаеле

**http://localhost:8000/api/profile/**

- Запрос GET Bearer Token: "ACCESS_TOKEN"

Ответ, если токен действителен
```json
{
    "phone": "user.phone",
    "email": "user.email",
    "first_name": "user.first_name",
    "last_name": "user_.last_name"
}
```
Ответ, если токен не действителен
```json
{
    "detail": "Given token not valid for any token type",
    "code": "token_not_valid",
    "messages": [
        {
            "token_class": "AccessToken",
            "token_type": "access",
            "message": "Token is invalid or expired"
        }
    ]
}
```
- Срок действия ACCESS токена 30 минут после истечения нужно его обновить на **http://localhost:8000/api/auth/refresh**
- Срок дейсвия REFRESH_TOKEN 7 дней после истечения нужно авторизоваться заново

# Товары

http://localhost:8000/api/v1/product/products/
```json
{
        "id": 2,
        "created_at": "06.02.2024",
        "name": "Брюки темные для мальчика",
        "description": "Состав:\r\n60% - хлопок \r\n30% - ткани\r\n10% - нитки",
        "tags": [
            {
                "name": "Брюки"
            },
            {
                "name": "Для мальчиков"
            }
        ],
        "count": 100,
        "size": [
            {
                "name": "XL"
            },
            {
                "name": "L"
            }
        ],
        "cost": 4500.0,
        "rating": 666,
        "promotion": true,
        "promotion_cost": 3000.0,
        "image": [
            {
                "image": "http://127.0.0.1:8000/media/product_images/large_2.jpg"
            },
            {
                "image": "http://127.0.0.1:8000/media/product_images/d5fcaf91b8476153f2e7ffa0e5966b8c.png"
            }
        ],
        "catalog": {
            "id": 2,
            "name": "Школьная Форма",
            "image": "http://127.0.0.1:8000/media/catalog_images/large_25.jpg",
            "subcatalog": {
                "id": 2,
                "name": "Брюки",
                "image": "http://127.0.0.1:8000/media/subcatalog_images/large_41.jpg"
            }
        }
    }
```

## Админка 
http://localhost:8000/admin/

**Login**: admin@admin.ru

**Password**: admin

# Docker

Для создания контейнера и запуска контейнера:

```docker-compose up --build```

