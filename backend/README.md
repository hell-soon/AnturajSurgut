# API

### Доступ к API
- Документация

    http://127.0.0.1:8000/api/redoc/ - Redoc
 
    http://127.0.0.1:8000/api/docs/ - Swagger
# Работа с пользователями
- Регистрация пользователей
    
    http://127.0.0.1:8000/api/auth/register/


- Запрос JSON на регистрацию
```JSON
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

    http://127.0.0.1:8000/api/auth/login/

- Запрос JSON на авторизацию
```JSON
{
    "email": "email",
    "password": "password"
}
```
#### Валидация:

- Поле Email

#### Ответ:
```JSON
{
    "refresh": "REFRESH_TOKEN",
    "access": "ACCESS_TOKEN"
}
```
### Смена пароля пользователя

Проходит в 2 этапа:

**URLS:**
Для запроса ссылки на смену пароля

- http://127.0.0.1:8000/api/auth/change/password/ 

Для завершения смены пароля
- http://127.0.0.1:8000/api/auth/change/password/{uid}/{token} 


#### Первый этап
Пользователь заполняет форму с полем Email.
- запрос на сервер:
```JSON
{
    "email": "email"
}
```

- Если такого аккаунта нет, то получаем ответ:
```JSON
{
    "email": [
        "Введите правильный адрес электронной почты."
    ]
}
```
- Поле не было заполнено
```JSON
{
    "email": [
        "Это поле не может быть пустым."
    ]
}
```
- Если зарегистрированный аккаунт существует, то ответ:
```JSON
{
    "message": "На указанную почту было отправленно письмо",
    "uid": "uid",
    "token": "token"
}
```
#### Второй этап
- Из полученого ответа поля ```uid``` ```token``` будут использоваться для завершения смены пароля по ссылке:

http://127.0.0.1:8000/api/auth/change/password/{uid}/{token}

- Запрос на сервер

```JSON
{
    "password": "password"
}
```
- Если токен неверный
```JSON
{
    "message": "Неверный токен для смены пароля"
}
```
- Пароль не прошел валидацию
```JSON
{
    "password": [
        "Пароль должен содержать не менее 8 символов"
    ]
}
```
Или
```JSON
{
    "password": [
        "Пароль не должен состоять только из цифр"
    ]
}
```
- Успешная смена пароля
```JSON
{
    "message": "Пароль успешно обновлен"
}
```
### Информация о пользовтаеле

**http://127.0.0.1:8000/api/profile/**

- Запрос GET Bearer Token: "ACCESS_TOKEN"

Ответ, если токен действителен
```JSON
{
    "user": {
        "id": 1,
        "first_name": "",
        "last_name": "",
        "email": "admin@admin.ru",
        "phone": null
    },
    "user_cart_id": 1,
    "favorites": []
}
```
Ответ, если токен не действителен
```JSON
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
- Срок действия ACCESS токена 30 минут после истечения нужно его обновить на **http://127.0.0.1:8000/api/auth/refresh**
- Срок дейсвия REFRESH_TOKEN 7 дней после истечения нужно авторизоваться заново



### Корзина пользователя
Корзина пользователя требует авторизации.

Что б получить содержимое корзины пользователя, нужно сделать запрос **http://localhost:8000/api/profile/cart/** Метод **GET**
## Добавление в корзину
Добавление товаров в корзину пользователя.

Запрос **http://localhost:8000/api/profile/add-to-cart/** **POST**
```JSON
{
    "product_id": product_id,
    "cart_id": cart_id,
    "quantity": quantity
}
```
- Ответ

```JSON
{
    "success": "Товар добавлен в корзину"
}
```
# Товары
## Отображени товара
http://127.0.0.1:8000/api/v1/product/products/
```JSON
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
## Избранное

- Добавление **http://127.0.0.1:8000/api/profile/favorite/add/**:

Запрос:
```JSON
{
    "product_id": "product_id"
}
```
Ответ:
```JSON
{
    "success": "Товар добавлен в избранное"
}
```

- Удаление **http://127.0.0.1:8000/api/profile/favorite/remove/**

Запрос:
```JSON
{
    "product_id": "product_id"
}
```
Ответ:
```JSON
{
    "success": "Товар удален из избранного"
}
```
## Админка 
http://127.0.0.1:8000/admin/

**Login**: admin@admin.ru

**Password**: admin

# Docker

Для создания контейнера:

```docker-compose build```

Для запуска контейнера

```docker-compose up```

