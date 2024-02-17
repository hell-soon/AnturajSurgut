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

# Товары
## Отображени товара
http://127.0.0.1:8000/api/v1/product/products/
```JSON

{
    "catalog_id": 1,
    "catalog_name": "Школьная Форма",
    "catalog_image": "http://127.0.0.1:8000/media/catalog_images/large_2.jpg",
    "subcatalog": {
        "subcatalog_id": 1,
        "subcatalog_name": "Брюки школьные",
        "subcatalog_image": "http://127.0.0.1:8000/media/subcatalog_images/aa0cd46cf06379ed7b4d503d02dc0ff9c6fb9f74_full.jpg",
        "products": [
            {
                "id": 1,
                "created_at": "13.02.2024",
                "name": "Брюки",
                "description": "asd\r\nDSA\r\nADS\r\n\r\nASD",
                "count": 123,
                "size": [
                    {
                        "name": "XXL"
                    },
                    {
                        "name": "XL"
                    }
                ],
                "cost": 3700.0,
                "rating": 123,
                "promotion": false,
                "promotion_cost": null,
                "image": [
                    {
                        "image": "http://127.0.0.1:8000/media/product_images/aa0cd46cf06379ed7b4d503d02dc0ff9c6fb9f74_full.jpg"
                    }
                ]
            }
        ]
    }
}
```


# ЗАКАЗ
## Коды:
#### ```order_type``` - Тип доставки:
```JSON
{
    "order_type": "1", - Самовывоз
    "order_type": "2", - Доставка до двери
    "order_type": "3", - Доставка транспортной компанией
}
```
#### ```order_face``` - Лицо заказчика:
```JSON
{
    "order_face": "1", - Юридическое лицо
    "order_face": "2", - Физическое лицо
}
```
- Тело запроса:
```JSON
{
    "user_initials": "ФИО",
    "user_communication": "email/phone", - Формат телефона +12345678901
    "products": [
        {"product_id": product_id, "quantity": quantity},
        {"product_id": product_id, "quantity": quantity},
    ],
    "order_type": "1",
    "order_address": "address",
    "order_face": "2",
    "order_additionalservices": [1, 2, 3], - Доп услуги выбранные при оформлении
    "comment": "Доставить заказ к заднему входу" - Коментарий к заказу. Может быть пустой
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

