"""
Test for models
"""

from django.test import TestCase
from django.contrib.auth import get_user_model

from core import models # noqa


def create_user(email="test@example.com", password="test123"):
    """Helper function to create a user"""
    return get_user_model().objects.create_user(email, password)


class ModelTestCases(TestCase):
    """
    Model Tests
    """

    def test_create_user_with_email_successful(self):
        """
        Test that creating a user with an email is successful
        """
        email = "test@example.com"
        password = "mypassword123"

        user = create_user(email, password)

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_user_email_is_normalized(self):
        """
        Test the email for a new user is normalized
        """
        sample_emails = [
            ["test1@EXAMPLE.com", "test1@example.com"],
            ["test2@EXAmPLe.com", "test2@example.com"],
            ["TEST3@EXAMPLE.com", "TEST3@example.com"],
            ["Test4@EXAMPLE.com", "Test4@example.com"],
            ["test5@eXAMPLE.COM", "test5@example.com"],
        ]

        for submitted_email, normalized_email in sample_emails:
            user = create_user(email=submitted_email)
            self.assertEqual(user.email, normalized_email)

    def test_create_user_without_email_raises_exception(self):
        """
        Test that creating a user without email fails
        """
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user('', 'test123')

    def test_create_superuser(self):
        """
        Test that creating a superuser is successful
        """
        email = "admin@example.com"
        password = "adminpassword123"
        user = get_user_model().objects.create_superuser(
            email, password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)
