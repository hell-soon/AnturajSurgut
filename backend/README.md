# API

### Доступ к API
- Документация

    http://localhost:8000/api/v1/redoc/ 
 
    http://localhost:8000/api/v1/docs/
# Работа с пользователями
- Регистрация пользователей
    
    http://localhost:8000/api/v1/user/register/


- Запрос JSON на регистрацию
```
  {
    "phone": "phone",
    "first_name": "first_name",
    "last_name": "last_name",
    "password": "password"
  }
  ```
#### Валидация:

- Телефон 11 символов
- Пароль не менее 8 символов

### Авторизация пользователей 

    http://localhost:8000/api/v1/user/login/

- Запрос JSON на авторизацию
```
{
    "phone": "phone",
    "password": "password"
}
```
#### Валидация:

- Телефон 11 символов, иначе ошибка

#### Ответ:
```
{
    "refresh": "TOKEN",
    "access": "TOKEN"
}
```


# Товары

http://localhost:8000/api/v1/product/

## Админка 
http://localhost:8000/admin/

**Login**: admin

**Password**: admin

# Docker

Для создания контейнера:

```docker-compose build```

Для запуска контейнера

```docker-compose up```

