import datetime

JWT_TOKENS = {
    "JWT_EXPIRATION_DELTA": datetime.timedelta(
        hours=5
    ),  # Срок действия Access Token на 5 часов
    "JWT_REFRESH_EXPIRATION_DELTA": datetime.timedelta(
        days=7
    ),  # Срок действия Refresh Token на 7 дней
    "JWT_ALLOW_REFRESH": True,  # Разрешить обновление токена
}
