"""
Test for streaming_platforms APIs
"""
from django.urls import reverse
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model
from streaming_platforms.models import Platform
from streaming_platforms.serializers import PlatformSerializer


PLATFORMS_URL = reverse("streaming_platforms:platform-list")


def plaform_detail_url(platform_id):
    """
    Return the URL for the platform detail
    """
    return reverse("streaming_platforms:platform-detail", args=[platform_id])


def create_user(email="test@example.com", password="test123", **other_data):
    """
    Helper function to create a user
    """
    return get_user_model().objects.create_user(
        email,
        password,
        **other_data
    )


def create_superuser(email="admin@test.com", password="test", **other_data):
    """
    Helper function to create a user
    """
    super_user = get_user_model().objects.create_superuser(
        email,
        password,
        **other_data
    )
    super_user.is_staff = True
    super_user.is_superuser = True
    super_user.save()

    return super_user


def send_multiple_requests_to_api_endpoint(endpoint, client, num_requests=11):
    """
    Helper function to send 11 requests to the API endpoint
    """
    for i in range(num_requests):
        res = client.get(endpoint)
    return res


def create_platform(name="Netflix", website='netflix.com', **other_data):
    """
    Helper function to create a platform
    """
    return Platform.objects.create(
        name=name,
        website=website,
        **other_data
    )


class PublicPlatformAPITestCases(TestCase):
    """
    Public Test Cases for streamplatform APIs
    """
    def setUp(self):
        self.client = APIClient()

    def test_anon_user_get_platforms_list(self):
        """
        Test anonymous user can get the list of platforms
        """
        create_platform()
        create_platform(name="Amazon Prime", website='amazon.com')

        platforms = Platform.objects.all().order_by('-id')
        serializer = PlatformSerializer(platforms, many=True)

        res = self.client.get(PLATFORMS_URL)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res.data), 2)
        self.assertEqual(res.data, serializer.data)

    def test_anon_user_retrive_platform_details(self):
        """
        Test authenticated user can retrieve the details of a platform
        """
        platform = create_platform()
        res = self.client.get(plaform_detail_url(platform.id))

        serializer = PlatformSerializer(platform)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_anon_user_throttling(self):
        """
        Test that an Anonymous user can't send more than \
            10 requests in a minute
        """
        res = send_multiple_requests_to_api_endpoint(
            endpoint=PLATFORMS_URL,
            client=self.client,
            num_requests=11
        )
        self.assertEqual(res.status_code, status.HTTP_429_TOO_MANY_REQUESTS)

    def test_anon_user_create_platform_fails(self):
        """
        Test that an anonymous user can't create a platform
        """
        payload = {
            "name": "Netflix",
            "website": "netflix.com",
            "about": "Netflix is an online movie streaming platform"
        }

        res = self.client.post(PLATFORMS_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)


class PrivatePlatformAPITestCases(TestCase):
    """
    Private Test Cases for streamplatform APIs
    """
    def setUp(self):
        self.client = APIClient()
        self.user = create_user()
        self.client.force_authenticate(self.user)

        self.admin_client = APIClient()
        self.superuser = create_superuser()
        self.admin_client.force_authenticate(self.superuser)

    def test_auth_user_get_platforms_list(self):
        """
        Test authenticated user can get the list of platforms
        """
        create_platform()
        create_platform(name="Amazon Prime", website='amazon.com')

        platforms = Platform.objects.all().order_by('-id')
        serializer = PlatformSerializer(platforms, many=True)

        res = self.client.get(PLATFORMS_URL)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res.data), 2)
        self.assertEqual(res.data, serializer.data)

    def test_auth_user_retrive_platform_details(self):
        """
        Test authenticated user can retrieve the details of a platform
        """
        platform = create_platform()
        res = self.client.get(plaform_detail_url(platform.id))

        serializer = PlatformSerializer(platform)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_auth_user_throttling(self):
        """
        Test that an authenticated user can't send more than \
            30 requests in a minute
        """
        res = send_multiple_requests_to_api_endpoint(
            endpoint=PLATFORMS_URL,
            client=self.client,
            num_requests=31
        )
        self.assertEqual(res.status_code, status.HTTP_429_TOO_MANY_REQUESTS)

    def test_nromal_auth_user_create_platform_fails(self):
        """
        Test that a normal authenticated user can't create a platform
        """
        payload = {
            "name": "Netflix",
            "website": "netflix.com",
            "about": "Netflix is an online movie streaming platform"
        }

        res = self.client.post(PLATFORMS_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)

    def test_admin_user_create_platform(self):
        """
        Test that an admin user can create a platform
        """

        payload = {
            "name": "Disney+",
            "website": "https://www.disneyplus.com/",
            "about": "Disney+ is an online movie streaming platform"
        }

        res = self.admin_client.post(PLATFORMS_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

        self.user.is_staff = False
        self.user.save()
