# """
# Test for the Users API
# """

# from django.urls import reverse
# from django.test import TestCase
# from django.contrib.auth import get_user_model

# from rest_framework import status
# from rest_framework.test import APIClient


# CREATE_USER_URL = reverse("users:create")
# TOKEN_URL = reverse("users:token")
# MANAGE_PROFILE_URL = reverse("users:me")


# def create_user(email="test@example.com", password="test123", **other_data):
#     """
#     Helper function to create a user
#     """
#     return get_user_model().objects.create_user(
#         email,
#         password,
#         **other_data
#     )


# class PubliUsersApiTests(TestCase):
#     """
#     Test the publicly available users API
#     """

#     def setUp(self):
#         self.client = APIClient()

#     def test_create_valid_user_success(self):
#         """
#         Test creating user with valid payload is successful
#         """
#         payload = {
#             'email': 'test@example.com',
#             'password': 'test123',
#             'name': 'Test User'
#         }

#         res = self.client.post(CREATE_USER_URL, payload)
#         self.assertEqual(res.status_code, status.HTTP_201_CREATED)
#         self.assertNotIn("password", res.data)

#         user = get_user_model().objects.get(**res.data)
#         user_exists = get_user_model().objects.filter(
#             email=payload["email"]
#         ).exists()

#         self.assertTrue(user_exists)
#         self.assertTrue(user.check_password(payload['password']))

#     def test_user_with_email_exists_fails(self):
#         """
#         Test creating a user with an existing email fails
#         """
#         payload = {
#             'email': 'test@example.com',
#             'password': 'test123',
#             'name': 'Test User'
#         }

#         user = create_user(
#             email=payload["email"],
#             password=payload["password"]
#         )

#         res = self.client.post(CREATE_USER_URL, payload)

#         self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
#         user_exists = get_user_model().objects.filter(
#             id=user.id,
#             email=user.email,
#         ).exists()
#         self.assertTrue(user_exists)
#         users_with_the_email_count = get_user_model().objects.filter(
#             email=payload["email"]
#         ).count()
#         self.assertEqual(users_with_the_email_count, 1)

#     def test_password_too_short_error(self):
#         """
#         Test that the password must be more than 5 characters
#         """
#         payload = {
#             'email': 'test@example.com',
#             'password': 'p123',
#             'name': 'Test User'
#         }

#         res = self.client.post(CREATE_USER_URL, payload)

#         self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
#         user_exists = get_user_model().objects.filter(
#             email=payload['email']
#         ).exists()
#         self.assertFalse(user_exists)

#     def test_create_token_for_user(self):
#         """
#         Test that a token is created for the user.
#         """
#         user_details = {
#             'email': 'test@example.com',
#             'password': 'p123',
#             'name': 'Test User'
#         }

#         create_user(**user_details)

#         payload = {
#             'email': user_details['email'],
#             'password': user_details['password']
#         }

#         res = self.client.post(TOKEN_URL, payload)

#         self.assertEqual(res.status_code, status.HTTP_200_OK)
#         self.assertIn('token', res.data)

#     def test_create_token_invalid_credentials(self):
#         """
#         Test that token is not created for invalid credentials
#         """
#         user_details = {
#             'name': 'Test User',
#             'email': 'test@example.com',
#             'password': 'test123'
#         }

#         create_user(**user_details)

#         payload = {
#             'email': user_details['email'],
#             'password': 'wrongpassword'
#         }

#         res = self.client.post(TOKEN_URL, payload)

#         self.assertNotIn('token', res.data)
#         self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

#     def test_create_token_blank_password(self):
#         """
#         Test that token is not created for blank password
#         """
#         payload = {
#             'email': 'test@example.com',
#             'password': ''
#         }

#         res = self.client.post(TOKEN_URL, payload)

#         self.assertNotIn('token', res.data)
#         self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

#     def test_retrieve_user_unauthorized(self):
#         """
#         Test that authentication is required for users
#         """
#         res = self.client.get(MANAGE_PROFILE_URL)

#         self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)


# class PrivateUserApiTests(TestCase):
#     """
#     Test API requests that require authentication
#     """
#     def setUp(self):
#         self.user = create_user(name="Test User")
#         self.client = APIClient()
#         self.client.force_authenticate(user=self.user)

#     def test_post_request_not_allowed(self):
#         """
#         Test that POST is not allowed on the me URL
#         """
#         res = self.client.post(MANAGE_PROFILE_URL, {})

#         self.assertEqual(res.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

#     def test_retrieve_profile_success(self):
#         """
#         Test retrieving profile for logged in user
#         """
#         res = self.client.get(MANAGE_PROFILE_URL)

#         self.assertEqual(res.status_code, status.HTTP_200_OK)
#         self.assertEqual(res.data, {
#             'name': self.user.name,
#             'email': self.user.email
#         })

#     def test_update_user_profile(self):
#         """
#         Test updating the user profile for authenticated user
#         """
#         payload = {
#             'name': 'New Name',
#             'password': 'newpassword123'
#         }
#         res = self.client.patch(MANAGE_PROFILE_URL, payload)

#         self.user.refresh_from_db()
#         self.assertEqual(res.status_code, status.HTTP_200_OK)
#         self.assertEqual(self.user.name, payload["name"])
#         self.assertTrue(self.user.check_password(payload["password"]))
