# # Используем официальный образ Python
# FROM python:3.12-slim

# # Устанавливаем рабочую директорию
# WORKDIR /backend

# # Копируем зависимости и устанавливаем их
# COPY requirements.txt .
# RUN pip install --no-cache-dir -r requirements.txt

# # Копируем исходный код
# COPY . .

# # Статика
# # RUN python manage.py collectstatic --noinput
# # RUN python manage.py bot 
# # Экспортируем порт
# EXPOSE 8000


# # Выполняем запуск команды для запуска приложения
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]


FROM python:3.12-slim
ENV PYTHONUNBUFFERED 1
RUN mkdir /backend
WORKDIR /backend
ADD requirements.txt /backend/
COPY start.sh /start.sh

RUN pip install -r requirements.txt
ADD . /backend
RUN ls -all
CMD ["/start.sh"]