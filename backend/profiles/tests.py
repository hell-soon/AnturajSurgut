from django.urls import reverse

from rest_framework import status

from users.tests import Setup


class UserTestCase(Setup):
    def test_successful_get_user_info(self):
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + self.token)
        response_first = self.client.get(reverse("user_info"))
        response_second = self.client.get(reverse("user_info") + "?user_orders=true")

        self.assertEqual(response_first.status_code, status.HTTP_200_OK)
        self.assertEqual(response_second.status_code, status.HTTP_200_OK)

    def test_unsuccessful_get_user_info(self):
        response = self.client.get(reverse("user_info") + "?user_orders=true")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_unsuccessful_get_user_info2(self):
        response = self.client.get(reverse("user_info"))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_successful_change_user_info(self):
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + self.token)
        response = self.client.patch(
            reverse("user_change"),
            data={
                "first_name": "Test",
                "last_name": "User",
                "phone": "19003454156",
                "email": "change@email.com",
            },
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
