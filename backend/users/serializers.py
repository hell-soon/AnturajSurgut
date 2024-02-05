from django.utils.text import slugify
from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate
from django.db import IntegrityError


def format_phone(phone):
    """
    Проверка телефона на правильность
    Формат +7-999-999-99-99
    :param phone:
    :return: formatted_phone:
    """
    if not phone.isdigit():
        raise serializers.ValidationError("Телефон должен содержать только цифры")

    if len(phone) != 11:
        raise serializers.ValidationError("Телефон должен содержать 11 цифр")

    formatted_phone = f"+7-{phone[1:4]}-{phone[4:7]}-{phone[7:9]}-{phone[9:]}"
    return formatted_phone


class UserRegisterSerializer(serializers.ModelSerializer):
    phone = serializers.CharField()

    class Meta:
        model = get_user_model()
        fields = ['phone', 'password', 'first_name', 'last_name']
        extra_kwargs = {'password': {'write_only': True}}

    def validate_password(self, value):
        """
        Проверка пароля
        Можно добавить дополнительные проверки
        :param value:
        :return: value:
        """
        if len(value) < 8:
            raise serializers.ValidationError("Пароль должен содержать не менее 8 символов")
        return value

    def validate_phone(self, value):
        """
        Проверка на уникальность телефона
        :param value:
        :return: formatted_phone:
        """
        formatted_phone = format_phone(value)
        if get_user_model().objects.filter(phone=formatted_phone).exists():
            raise serializers.ValidationError("Данный телефон уже зарегистрирован")
        return formatted_phone

    def validate(self, data):
        """
        Проверка наличия имени и фамилии
        Важные поля т.к используются для генерации username
        :param data:
        :return: data:
        """
        if not data.get('first_name') or not data.get('last_name'):
            raise serializers.ValidationError("Необходимо указать имя и фамилию")
        return data

    def create(self, validated_data):
        """
        Создание пользователя после всех проверок
        Генерация username т.к мы его не будем использовать
        :param validated_data:
        :return:
        """
        phone = validated_data.pop('phone')  # Удаляем телефон из валидированных данных
        first_name = validated_data.get('first_name')
        last_name = validated_data.get('last_name')

        base_username = slugify(f"{first_name}-{last_name}")
        username = base_username
        suffix = 1

        while get_user_model().objects.filter(username=username).exists():
            username = f"{base_username}-{suffix}"
            suffix += 1

        try:
            # Передаем телефон при создании пользователя
            user = get_user_model().objects.create_user(username=username, phone=phone, **validated_data)
        except IntegrityError as e:
            raise serializers.ValidationError("Произошла ошибка на стороне сервера")

        return user


class UserLoginSerializer(serializers.Serializer):
    phone = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        """
        Валидность данных для аутентификации
        Можно добавить дополнительные проверки
        :param data:
        :return:
        """
        phone = data.get('phone')
        password = data.get('password')
        if len(phone) != 11:
                raise serializers.ValidationError("Телефон должен содержать 11 цифр")
        if phone and password:
            formatted_phone = f"+7-{phone[1:4]}-{phone[4:7]}-{phone[7:9]}-{phone[9:]}"
            user = authenticate(phone=formatted_phone, password=password)
            if not user:
                raise serializers.ValidationError("Неверные учетные данные")
        else:
            raise serializers.ValidationError("Требуется указать номер телефона и пароль")

        data['user'] = user
        return data
