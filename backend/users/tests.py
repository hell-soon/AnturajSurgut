from django.test import TestCase, Client
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import CustomUser
from icecream import ic


# ТЕСТЫ НА ПРОВЕРКУ СИСТЕМУ АВТОРИЗАЦИИ
class CustomUserRegistrationTestCase(APITestCase):
    # ПОДГОТОВКА ДАННЫХ ДЛЯ ТЕСТА
    def setUp(self):
        self.client = Client()
        self.user = CustomUser.objects.create_user(
            email="nT0n7@example.com",
            password="TestPassword123",
            first_name="Test",
            last_name="User",
        )

    # Успешная авторизация
    def test_successful_login(self):
        response = self.client.post(
            reverse("login_user"),
            data={
                "email": "nT0n7@example.com",
                "password": "TestPassword123",
            },
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        return response.data

    # Неуспешная авторизация
    def test_unsuccessful_login(self):
        response = self.client.post(
            reverse("login_user"),
            data={
                "email": "nT0n7@example.com",
                "password": "wrongpassword",
            },
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    # Успешная регистрация
    def test_successful_register_user(self):
        response = self.client.post(
            reverse("register_user"),
            data={
                "email": "Test@mail.com",
                "password1": "TestPassworsadd123",
                "password2": "TestPassworsadd123",
                "first_name": "Test",
                "last_name": "User",
            },
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    # Неуспешная регистрация
    def test_unsuccessful_register_user(self):
        response = self.client.post(
            reverse("register_user"),
            data={
                "email": "Test@mail.com",
                "password1": "TestPassworsadd123",
                "password2": "TestPassworsadd12",
                "first_name": "Test",
                "last_name": "User",
            },
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_unsuccessful_register_user2(self):
        response = self.client.post(
            reverse("register_user"),
            data={
                "email": "nT0n7@example.com",
                "password1": "TestPassworsadd123",
                "password2": "TestPassworsadd123",
                "first_name": "Test",
                "last_name": "User",
            },
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    # Успешная смена пароля
    def test_successful_change_password(self):
        response_first = self.client.post(
            reverse("password_change_email"),
            data={"email": "nT0n7@example.com"},
        )
        self.assertEqual(response_first.status_code, status.HTTP_200_OK)
        uidb64 = response_first.data["uidb64"]
        token = response_first.data["token"]

        response_second = self.client.post(
            reverse("change_password", kwargs={"uidb64": uidb64, "token": token}),
            data={"password1": "TestPassworsadd123", "password2": "TestPassworsadd123"},
        )
        self.assertEqual(response_second.status_code, status.HTTP_200_OK)

    # Аккаунт с такой почтой не существует в базе
    def test_unsuccessful_change_password(self):
        response = self.client.post(
            reverse("password_change_email"),
            data={"email": "nT0n7@example123.com"},
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_successful_refresh_token(self):
        data = self.test_successful_login()
        responce = self.client.post(
            reverse("token_refresh"),
            data={"refresh": data["refresh"]},
        )
        self.assertEqual(responce.status_code, status.HTTP_200_OK)

    def test_unsuccessful_refresh_token(self):
        responce = self.client.post(
            reverse("token_refresh"),
            data={"refresh": "wrongrefresh"},
        )
        self.assertEqual(responce.status_code, status.HTTP_401_UNAUTHORIZED)
