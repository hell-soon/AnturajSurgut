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
        "id": 3,
        "first_name": "Test",
        "last_name": "123456",
        "email": "email@test.ru",
        "phone": "123567890"
    }
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
- Срок действия ACCESS токена 5 часов после истечения нужно его обновить на **http://127.0.0.1:8000/api/auth/refresh**
- Срок дейсвия REFRESH_TOKEN 7 дней после истечения нужно авторизоваться заново
### Изменение информацию о пользователе
- http://127.0.0.1:8000/api/profile/change/ Метод PATCH
- Тело запроса:
```JSON
{
    "first_name": "first_name",
    "last_name": "last_name",
    "phone": "phone",
    "email": "email"
}
```
**Дополнительно**

В запросе не обязательно указывать все 4 поля.
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
| Код | Описание |
| ----------- | ----------- |
| 1    | Самовывоз    |
| 2    | Доставка до двери    |
| 3    | Доставка транспортной компанией    |


#### ```order_face``` - Лицо заказчика:
| Код | Описание |
| ----------- | ----------- |
| 1    | Юридическое лицо    |
| 2    | Физическое лицо    |

### Основное тело запроса:
```JSON
{
{
    "user_initials": "John Doe",
    "user_email": "johndoe@example.com",
    "user_phone": "123456789",
    "items": [
        {
            "id": 1,
            "quantity": 2
        },
        {
            "id": 2,
            "quantity": 1
        }
    ],
    "order_additionalservices": [1,2,3],
    "order_type": "1",
    "order_address": "123 Main St",
    "order_face": "2",
    "comment": "Please deliver to the front door"
}
}
```
### Валидация:
- поля user_email и user_phone, должно быть заполнено хотя бы одно любое из этих полей

## Админка 
http://127.0.0.1:8000/admin/

**Login**: admin@admin.ru

**Password**: admin

# Docker

Для создания контейнера:

```docker-compose build```

Для запуска контейнера

```docker-compose up```

