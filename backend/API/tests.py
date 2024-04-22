from rest_framework.test import APITestCase

from django.contrib.auth import get_user_model
from django.core.management import call_command
from django.urls import reverse


class Setup(APITestCase):
    def setUp(self):
        call_command("create_data")
        self.user = get_user_model().objects.create_user(
            email="nT0n7@example.com",
            password="TestPassword123",
            first_name="Test",
            last_name="User",
        )

        response = self.client.post(
            reverse("login_user"),
            data={
                "email": self.user.email,
                "password": "TestPassword123",
            },
        )
        self.token = response.data["access"]
        self.refresh = response.data["refresh"]
