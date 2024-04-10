"""
Movies App Models
"""
from django.db import models
from core.models import User
from casts.models import Cast
from streaming_platforms.models import Platform

from django.contrib.contenttypes.fields import (
    GenericForeignKey,
    GenericRelation
)
from django.contrib.contenttypes.models import ContentType
from django.db.models.signals import post_save
from django.dispatch import receiver


class Genre(models.Model):
    """
    Model for Genres
    """
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=100, blank=True)

    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name


class Movie(models.Model):
    """
    Model for Movies
    """

    BBFC_RATINGS = [
        ('U', 'Universal - Suitable for all ages.'),
        ('PG', 'Parental Guidance - Scenes may be unsuitable for children.'),
        ('12', '12A/12 - Suitable for 12 years and over.'),
        ('15', '15 - Suitable only for 15 years and over.'),
        ('18', '18 - Suitable only for adults.'),
        ('R18', 'Restricted 18 - Only available in licensed premises'),
        ('E', 'Exempt - Not subject to classification.'),
        ('TBC', 'To Be Confirmed - Rating is yet to be determined.'),
    ]

    CONTENT_TYPES = [
        ('Movies', 'Movies'),
        ('TV_series', 'TV Series'),
        ('Film_Series', 'Film Series'),
        ('Episodes', 'Episodes'),
        ('Documentaries', 'Documentaries'),
    ]

    title = models.CharField(max_length=100, blank=False)
    intro = models.CharField(max_length=100, blank=True)
    storyline = models.TextField(max_length=1500, blank=True)
    year = models.IntegerField()
    duration = models.IntegerField(help_text="Duration in minutes")
    genres = models.ManyToManyField(Genre, related_name='movies')
    content_type = models.CharField(max_length=20, choices=CONTENT_TYPES)
    bbfc_rating = models.CharField(
        max_length=4,
        default='U',
        verbose_name='BBFC Rating',
        choices=BBFC_RATINGS,
        help_text='Select the BBFC rating for this movie.',
    )
    avg_rating = models.FloatField(default=0)
    rating_count = models.PositiveIntegerField(default=0)
    actors = models.ManyToManyField(Cast, related_name='acted_movies')
    starring = models.ManyToManyField(Cast, related_name='starred_movies')
    directors = models.ManyToManyField(Cast, related_name='directed_movies')
    platform = models.ForeignKey(
        Platform,
        on_delete=models.CASCADE,
        related_name='movies'
    )
    views = GenericRelation('ContentView')
    reviews = GenericRelation('Review')

    popularity = models.DecimalField(max_digits=5, decimal_places=2, default=0)

    is_active = models.BooleanField(default=True)
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    @property
    def views_count(self):
        return self.views.count()

    def recent_views(self, limit=10):
        return self.views.order_by('-viewed_at')[:limit]

    def popularity_score(self):
        return self.popularity * 100

    def save(self, *args, **kwargs):
        if self.title == '':
            raise ValueError("Title is required")
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        if self.intro:
            return f"{self.title}: {self.intro} ({self.year})"
        return self.title


class Season(models.Model):
    """
    Model for TV Series Seasons
    """
    title = models.CharField(max_length=100, blank=False)
    intro = models.CharField(max_length=100, blank=True)
    storyline = models.TextField(max_length=1000, blank=True)
    duration = models.IntegerField(help_text="Duration in minutes")
    movie = models.ForeignKey(
        Movie,
        on_delete=models.CASCADE,
        related_name='seasons'
    )
    avg_rating = models.FloatField(default=0)
    rating_count = models.PositiveIntegerField(default=0)
    views = GenericRelation('ContentView')
    reviews = GenericRelation('Review')
    popularity = models.DecimalField(max_digits=5, decimal_places=2, default=0)

    is_active = models.BooleanField(default=True)
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    @property
    def views_count(self):
        return self.views.count()

    def recent_views(self, limit=10):
        return self.views.order_by('-viewed_at')[:limit]

    def popularity_score(self):
        return self.popularity * 100

    def save(self, *args, **kwargs):
        if self.title == '':
            raise ValueError("Title is required")
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f"{self.movie.title} ({self.title})"


class Episode(models.Model):
    """
    Model for Movie Episodes
    """
    title = models.CharField(max_length=100, blank=False)
    intro = models.CharField(max_length=100, blank=True)
    storyline = models.TextField(max_length=1000, blank=True)
    duration = models.IntegerField(help_text="Duration in minutes")
    season = models.ForeignKey(
        Season,
        on_delete=models.CASCADE,
        related_name='episodes'
    )
    avg_rating = models.FloatField(default=0)
    rating_count = models.PositiveIntegerField(default=0)
    views = GenericRelation('ContentView')
    reviews = GenericRelation('Review')
    popularity = models.DecimalField(max_digits=5, decimal_places=2, default=0)

    is_active = models.BooleanField(default=True)
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    @property
    def views_count(self):
        return self.views.count()

    def recent_views(self, limit=10):
        return self.views.order_by('-viewed_at')[:limit]

    def popularity_score(self):
        return self.popularity * 100

    def save(self, *args, **kwargs):
        if self.title == '':
            raise ValueError("Title is required")
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f"{str(self.season)} - {self.title}"


class ContentView(models.Model):
    """
    Model to Track Content (Movies, Seasons, Episodes) Views
    """
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content = GenericForeignKey('content_type', 'object_id')
    viewed_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        default=None
    )
    viewed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        if self.viewed_by is None:
            return f"{self.content.title} Viewed by Anonymous at \
                {self.viewed_at}"

        return f"{self.content.title} Viewed by {self.viewed_by.email}\
            at {self.viewed_at}"


# ! You'll need this, man!!
# e = Episode.objects.create(season=my_season, ...)
# p = Production.objects.create(
#     p_type=ContentType.objects.get_for_model(Episode), object_id=e.pk)


class Review(models.Model):
    """
    Model for Reviews
    """
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content = GenericForeignKey('content_type', 'object_id')
    rating = models.PositiveIntegerField()
    comment = models.TextField(max_length=500)

    is_active = models.BooleanField(default=True)
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        film_title = self.content_type.get_object_for_this_type(
            id=self.object_id
        ).title
        return f"{film_title} ({self.rating})"


@receiver(post_save, sender=ContentView)
def update_popularity_score(sender, instance, **kwargs):
    content_model = instance.content_type.model_class()
    max_views_count = content_model.objects.aggregate(
        max_views=models.Max('views_count')
    )['max_views']
    normalized_views = 0
    if max_views_count:
        normalized_views = instance.views_count / max_views_count
    content_instance = instance.content
    content_instance.popularity = normalized_views
    content_instance.save()
