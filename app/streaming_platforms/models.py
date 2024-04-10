"""
Models for the Streaming Platforms App.
"""
from django.db import models


class Platform(models.Model):
    """
    Model for Streaming Platforms.
    """
    name = models.CharField(max_length=100)
    about = models.TextField(max_length=1000)
    website = models.URLField()

    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    @property
    def movies_count(self):
        return self.movies.count()
