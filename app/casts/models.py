"""
Models for the Cast App.
"""
from django.db import models
from django.urls import reverse

# from movies.models import Movie


class Cast(models.Model):
    """
    Model for the Cast App.
    """
    GENDER = [
        ('M', 'Male'),
        ('F', 'Female')
    ]

    ROLE = [
        ('actor', 'Actor'),
        ('director', 'Director')
    ]

    name = models.CharField(max_length=100)
    well_known_as = models.CharField(max_length=100, blank=True)
    age = models.IntegerField()
    gender = models.CharField(max_length=20, choices=GENDER)
    bio = models.TextField(max_length=1500)
    role = models.CharField(max_length=100, choices=ROLE)
    movies = models.ManyToManyField('movies.Movie', related_name='casts')
    awards = models.ManyToManyField('Award', through='AwardReceived')
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    # @property
    # def movies(self):
    #     return Movies.objects.filter()

    def get_absolute_url(self):
        return reverse("cast-detail", kwargs={"id": self.id})

    def __str__(self) -> str:
        return self.name


class Award(models.Model):
    """
    Model for Awards won by casts
    """
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    description = models.TextField(max_length=500)

    is_active = models.BooleanField(default=True)
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse("award-detail", kwargs={"id": self.id})

    def __str__(self) -> str:
        return f"{self.name} - {self.category}"


class AwardReceived(models.Model):
    recipient = models.ForeignKey(Cast, on_delete=models.CASCADE)
    award = models.ForeignKey(Award, on_delete=models.CASCADE)
    year_received = models.PositiveIntegerField()

    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ['recipient', 'award']
        verbose_name_plural = 'Awards Received'

    def get_absolute_url(self):
        return reverse("award-received-detail", kwargs={"id": self.id})

    def __str__(self) -> str:
        return f"{self.recipient.name} - {self.award.name}"
