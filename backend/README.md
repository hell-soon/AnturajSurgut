# API

### Доступ к API
- Документация

    http://127.0.0.1:8000/api/redoc/ - Redoc
 
    http://127.0.0.1:8000/api/docs/ - Swagger
# Работа с пользователями
- Регистрация пользователей
    
    http://127.0.0.1:8000/api/v1/auth/register/


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

    http://127.0.0.1:8000/api/v1/auth/login/

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

- http://127.0.0.1:8000/api/v1/auth/change/password/ 

Для завершения смены пароля
- http://127.0.0.1:8000/api/v1/auth/change/password/{uid}/{token} 


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

**http://127.0.0.1:8000/api/v1/profile/**

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
- Срок действия ACCESS токена 5 часов после истечения нужно его обновить на **http://127.0.0.1:8000/api/v1/auth/refresh**
- Срок дейсвия REFRESH_TOKEN 7 дней после истечения нужно авторизоваться заново
### Изменение информацию о пользователе
- http://127.0.0.1:8000/api/v1/profile/change/ Метод PATCH
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
http://127.0.0.1:8000/api/v1/list/product/
```JSON
{
    "catalog": {
        "id": 2,
        "name": "фывфывыф",
        "image": "http://127.0.0.1:8000/media/catalog_images/DcwqgdOMiFw.jpg",
        "subcatalog": {
            "id": 2,
            "name": "фывфыв",
            "image": "http://127.0.0.1:8000/media/subcatalog_images/c-NKb-usMu0.jpg"
        }
    },
    "product": {
        "id": 2,
        "name": "фыв",
        "description": "фывфыв",
        "image": [
            {
                "image": "http://127.0.0.1:8000/media/product_images/dStUSAf-CiU.jpg"
            }
        ],
        "tags": [
            {
                "name": "asdsadadsad"
            }
        ],
        "product_status": true,
        "created_at": "24.02.2024"
    }
}
```
### Дополнительная информация о товаре:
http://127.0.0.1:8000/api/v1/list/product/info/{product_id}/
```JSON
[
    {
        "product_info_id": 2,
        "color": {
            "id": 1,
            "name": "asdsad",
            "code": "sadsadsa"
        },
        "size": {
            "id": 1,
            "name": "asdasdsad"
        },
        "quantity": -156,
        "cost": 111.0,
        "promotion": false,
        "promotion_cost": 1111.0
    },
    {
        "product_info_id": 3,
        "color": {
            "id": 2,
            "name": "asdasdsadasdasd",
            "code": "asdsadsad"
        },
        "size": {
            "id": 1,
            "name": "asdasdsad"
        },
        "quantity": 9975,
        "cost": 1111.0,
        "promotion": true,
        "promotion_cost": 300.0
    }
]
```
# ЗАКАЗ
### Основное тело запроса:
```JSON
{
    "user_initials": "John Doe",
    "user_email": "WinerTy@yan1dex.ru",
    "user_phone": "",
    "items": [
        {
            "product_info_id": 2,
            "quantity": 5
        },
        {
            "product_info_id": 4,
            "quantity": 5
        }
    ],
    "order_additionalservices": [1],
    "order_type": "1",
    "order_address": "123 Main St",
    "order_face": "2",
    "comment": "Please deliver to the front door"
}
```
| поле | описание | тип|
|------|----------|----|
| user_initials | Инициалы заказчика |string|
|user_email| Почта заказчика |string|
|user_phone| телефон заказчика|string|
|items| товары |string|
|items[product_info_id]| id дополнительной информации о товаре [тут](http://127.0.0.1:8000/api/v1/list/product/info/{product_id}/)|int|
|item[quanity]| количество товара|int|
|order_additionalservices| дополнительные услуги к заказу (Список с их id)|int|
|order_type|id типа заказа(Описан ниже)|int|
|order_address| Адресс доставки|string|
|order_face|Тип заказчика(описан ниже)|int|
|comment| Коментарий заказчика|string|

## Коды:
#### ```order_additionalservices```
Весь список активных доп услуг - http://localhost:8000/api/v1/order/service/
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

### Валидация:
- поля user_email и user_phone, должно быть заполнено хотя бы одно любое из этих полей

### Изменение заказа:
Тело запроса:
```JSON
{
    "items": [
        {
            "product_info_id": 3,
            "quantity": 90
        },
        {
            "product_info_id": 4,
            "quantity": 90
        }
    ],
    "order_additionalservices": [1,2,4],
    "order_status": "5"
}
```
|Поле| валидация| описание |
|----|----------|----------|
|items|Выдает ошибку если количество товара в заказе превышает его количество на складе|Передается id подробной информации товара и его количество или товар был удален|
|order_additionalservices|Ошибка если указанный id доп.услуги не был найден| список id с теми доп услугами которые выбрал пользователь к своему заказу|
|order_status|Ошибка если пользователь захотел отменить заказ статус которого отличен от статуса "Не готов" или заказ уже был отменен|Передаеться ключ значение для отмены, ключ - 5|

**ДОПОЛНИТЕЛЬНО**

Передается id не ТОВАРА а id информации о товаре, это связана с тем, что у товара есть пречень Цветов, размеров и тд, и у каждого цвета или размера разная стоимость и разное количество товара на складе. ID Информации о товаре уникален, поэтому не нужно передавать Id цвета и тд, все это уже храниться в передаваемом id информации о товаре.

Информацию о доп информации о товаре можно получить тут http://127.0.0.1:8000/api/v1/list/product/info/{product_id}/
## Админка 
http://127.0.0.1:8000/admin/

**Login**: admin@admin.ru

**Password**: admin

# Docker

Для создания контейнера:

```docker-compose build```

Для запуска контейнера

```docker-compose up```

