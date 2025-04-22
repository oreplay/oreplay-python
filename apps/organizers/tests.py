import uuid

from django.urls import reverse
from django.utils.timezone import now, timedelta
from rest_framework import status
from rest_framework.test import APITestCase

from apps.organizers.models import Organizer
from apps.users.models import AccessToken, User


class OrgainzerViewSetTests(APITestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create(email="test@user.com", password="password123")
        # Create a valid token
        self.token = AccessToken.objects.create(
            user=self.user,
            access_token="valid_token",
            expires=now() + timedelta(hours=1),
        )
        # Create an expired token
        self.expired_token = AccessToken.objects.create(
            user=self.user,
            access_token="expired_token",
            expires=now() - timedelta(hours=1),
        )

        self.organizer = Organizer.objects.create(
            name="Test", external_id="01", country="ES"
        )

        self.url = reverse("organizer-list")

        self.organizer_data = {
            "id": uuid.uuid4(),
            "external_id": "00",
            "name": "Test organizer",
            "country": "ES",
        }

    def test_get_list(self):
        self.client.credentials(HTTP_AUTHORIZATION="Bearer valid_token")
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()), 1)

    def test_get_retrieve(self):
        url = self.url + str(self.organizer.id) + "/"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()["id"], str(self.organizer.id))

    def test_get_retrive_not_found(self):
        url = self.url + str(uuid.uuid4()) + "/"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_post_with_valid_token(self):
        self.client.credentials(HTTP_AUTHORIZATION="Bearer valid_token")
        response = self.client.post(self.url, data=self.organizer_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.json()["name"], self.organizer_data["name"])

    def test_post_with_invalid_token(self):
        self.client.credentials(HTTP_AUTHORIZATION="Bearer invalid_token")
        response = self.client.post(self.url, data=self.organizer_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(response.json()["error"], "Invalid token")

    def test_post_with_expired_token(self):
        self.client.credentials(HTTP_AUTHORIZATION="Bearer expired_token")
        response = self.client.post(self.url, data=self.organizer_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(response.json()["error"], "The token has expired.")

    def test_put_with_valid_token(self):
        url = self.url + str(self.organizer.id) + "/"
        updated_data = {
            "name": "Updated Organizer",
            "external_id": "02",
            "country": "US",
        }
        self.client.credentials(HTTP_AUTHORIZATION="Bearer valid_token")
        response = self.client.put(url, data=updated_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()["name"], updated_data["name"])

    def test_put_with_invalid_token(self):
        url = self.url + str(self.organizer.id) + "/"
        updated_data = {
            "name": "Updated Organizer",
            "external_id": "02",
            "country": "US",
        }
        self.client.credentials(HTTP_AUTHORIZATION="Bearer invalid_token")
        response = self.client.put(url, data=updated_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(response.json()["error"], "Invalid token")

    def test_put_with_expired_token(self):
        url = self.url + str(self.organizer.id) + "/"
        updated_data = {
            "name": "Updated Organizer",
            "external_id": "02",
            "country": "US",
        }
        self.client.credentials(HTTP_AUTHORIZATION="Bearer expired_token")
        response = self.client.put(url, data=updated_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(response.json()["error"], "The token has expired.")
