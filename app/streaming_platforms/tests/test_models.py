"""
Test for Stream Platforms Models
"""
from django.test import TestCase
from streaming_platforms.models import Platform


class PlatformTestCases(TestCase):
    """
    Test cases for the Platform model.
    """
    def test_creating_a_platform(self):
        """
        Test that creating a platform is successful
        """
        name = 'Netflix'
        about = 'Netflix is an online movie streaming platform'

        netflix = Platform.objects.create(
            name=name,
            website='netflix.com',
            about=about
        )

        self.assertEqual(netflix.name, name)
        self.assertEqual(netflix.about, about)
        self.assertEqual(str(netflix), name)
        self.assertTrue(Platform.objects.count())
