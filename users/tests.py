from django.test import TestCase, Client
from django.urls import reverse

from . import models


class RegistrationTestCase(TestCase):
    """
    This tests the registration process.
    """

    def setUp(self):
        self.client = Client()

    def test_registration_view(self):
        response = self.client.get(reverse("register"))

        self.assertContains(response, "<form")
        self.assertEqual(response.status_code, 200)
