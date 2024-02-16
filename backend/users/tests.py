from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import CustomUser


class CustomUserRegistrationTestCase(APITestCase):
    def test_user_registration(self):
        url = reverse("register")
        data = {
            "email": "testuser@example.com",
            "password": "testpassword123",
            "first_name": "Test",
            "last_name": "User",
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue("email" in response.data)
        self.assertEqual(response.data["email"], data["email"])
        self.assertFalse("password" in response.data)
        print("Успешная регистрация пользователя")

    def test_user_login(self):
        # Создание пользователя для аутентификации
        CustomUser.objects.create_user(
            email="loginuser@example.com",
            password="loginpassword123",
            first_name="Login",
            last_name="User",
        )

        # Авторизация пользователя
        url = reverse("user_login")
        data = {
            "email": "loginuser@example.com",
            "password": "loginpassword123",
        }
        response = self.client.post(url, data, format="json")

        # Проверка успешной аутентификации
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue("access" in response.data)
        print("Успешная аутентификация пользователя")

    def test_user_info(self):
        # Создание пользователя для аутентификации
        user = CustomUser.objects.create_user(
            email="infouser@example.com",
            password="infopassword123",
            first_name="Info",
            last_name="User",
        )

        # Получение токена JWT для созданного пользователя
        url_login = reverse("user_login")
        login_data = {
            "email": "infouser@example.com",
            "password": "infopassword123",
        }
        login_response = self.client.post(url_login, login_data, format="json")
        access_token = login_response.data["access"]

        # Использование токена JWT для аутентификации при запросе информации о пользователе
        url_info = reverse(
            "user_info"
        )  # предполагается, что у вас есть URL с именем 'user_info'
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + access_token)
        info_response = self.client.get(url_info)

        # Проверка получения информации о пользователе
        self.assertEqual(info_response.status_code, status.HTTP_200_OK)
        self.assertEqual(info_response.data["user"]["email"], user.email)
        self.assertEqual(info_response.data["user"]["first_name"], user.first_name)
        self.assertEqual(info_response.data["user"]["last_name"], user.last_name)
        self.assertEqual(info_response.data["user_cart_id"], user.cart.id)
        print("Успешный запрос информации о пользователе с использованием JWT токена")

    def test_user_info_without_token(self):
        user = CustomUser.objects.create_user(
            email="infouser@example.com",
            password="infopassword123",
            first_name="Info",
            last_name="User",
        )
        url_info = reverse("user_info")
        info_response = self.client.get(url_info)

        # Проверка получения информации о пользователе
        self.assertEqual(info_response.status_code, status.HTTP_401_UNAUTHORIZED)
        print("Запрос без JWT токена невозможен")
