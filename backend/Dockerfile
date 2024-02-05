# Используем официальный образ Python
FROM python:3.12-slim

# Устанавливаем рабочую директорию
WORKDIR /backend

# Копируем зависимости и устанавливаем их
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем исходный код
COPY . .

# Статика
RUN python manage.py collectstatic --noinput
RUN python manage.py makemigrations users
RUN python manage.py makemigrations database
RUN python manage.py makemigrations sitedb
RUN python manage.py migrate

# Экспортируем порт
EXPOSE 8000


# Выполняем миграции, создаем суперпользователя и запускаем приложение
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]