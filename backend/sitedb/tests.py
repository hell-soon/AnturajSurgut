from django.urls import reverse

from rest_framework import status

from users.tests import Setup
from icecream import ic


class SiteTestCase(Setup):
    def test_get_sliders(self):
        response = self.client.get(reverse("slider-list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_contacts(self):
        url = reverse("contact-list")
        response_first = self.client.get(url)
        response_second = self.client.get(url + "?include_social=true")

        self.assertEqual(response_first.status_code, status.HTTP_200_OK)
        self.assertNotIn("social_accounts", response_first.data)
        self.assertEqual(response_second.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response_second.data["social_accounts"]), 2)
