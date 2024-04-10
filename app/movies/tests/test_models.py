"""
Test for the models in the movies app
"""
from movies.models import (
    Movie,
    Season,
    Episode,
    Genre,
    Review
)
from django.test import TestCase
from django.contrib.auth import get_user_model
from streaming_platforms.models import Platform
from django.contrib.contenttypes.models import ContentType


def create_platform():
    """
    Helper function to create a platform
    """
    return Platform.objects.create(
        name='Netflix',
        website='netflix.com',
        about='Netflix is an online movie streaming platform'
    )


def create_movie():
    """
    Helper function to create a movie
    """
    return Movie.objects.create(
        title="The Matrix",
        intro="Fight to survive.",
        year=1999,
        storyline="A computer hacker learns from mysterious \
        rebels about the true nature of his reality.",
        duration=136,
        platform=create_platform(),
        is_active=True,
    )


def create_season(movie=None):
    """
    Helper function to create a season
    """
    if movie is None:
        movie = create_movie()

    return Season.objects.create(
        title="Season 1",
        intro="The beginning of the end.",
        storyline="The first season of the series.",
        duration=100,
        movie=movie,
    )


def create_episode(season=None):
    """
    Helper function to create an episode
    """
    if season is None:
        season = create_season()

    return Episode.objects.create(
        title="Episode 1",
        intro="The beginning of the end.",
        storyline="The first episode of the series.",
        duration=45,
        season=season,
    )


def create_user(email="test@example.com", password="test123"):
    """
    Helper function to create a user
    """
    return get_user_model().objects.create_user(email, password)


class ModelTestCases(TestCase):
    """
    Movies App Models Tests
    """
    def test_creating_movie(self):
        """
        Test that creating a movie is successful
        """
        movie = create_movie()

        # self.assertEqual(movie.title, "The Matrix")
        self.assertEqual(movie.intro, "Fight to survive.")
        self.assertEqual(movie.year, 1999)
        self.assertEqual(movie.duration, 136)
        self.assertTrue(movie.date_added)
        self.assertTrue(movie.date_modified)
        self.assertTrue(movie.id)
        # self.assertEqual(
        #     str(movie), f"{movie.title}: {movie.intro} ({movie.year})")

    def test_creating_movie_without_title_raises_exception(self):
        """
        Test that creating a movie without title fails
        """
        with self.assertRaises(ValueError):
            Movie.objects.create(
                intro="Fight to survive.",
                year=1999,
                storyline="A computer hacker learns from mysterious \
                    rebels about the true nature of his reality.",
                duration=136,
                platform=create_platform(),
                is_active=True,
            )

    def test_creating_movie_season(self):
        """
        Test that creating a movie season is successful
        """
        movie = create_movie()
        season = create_season(movie=movie)

        self.assertEqual(season.title, "Season 1")
        self.assertEqual(movie.seasons.count(), 1)
        self.assertEqual(movie.seasons.first(), season)

    def test_creating_movie_season_episode(self):
        """
        Test that creating a movie season episode is successful
        """
        movie = create_movie()
        season = create_season(movie=movie)
        episode = create_episode(season=season)

        self.assertEqual(episode.title, "Episode 1")
        self.assertEqual(season.episodes.count(), 1)
        self.assertEqual(season.episodes.first(), episode)

    def test_creating_genre(self):
        """
        Test that creating a genre is successful
        """
        genre = Genre.objects.create(
            name="Action",
            description="Movies that are action-packed."
        )

        self.assertEqual(genre.name, "Action")
        self.assertTrue(genre.id)
        self.assertEqual(str(genre), genre.name)

    def test_creating_review(self):
        """
        Test that creating a review is successful
        """
        user = create_user()
        movie = create_movie()
        movie_content_type = ContentType.objects.get_for_model(Movie)
        review = Review.objects.create(
            author=user,
            content_type=movie_content_type,
            object_id=movie.id,
            rating=5,
            comment="Great movie!"
        )

        self.assertEqual(review.author, user)
        self.assertEqual(review.content_type, movie_content_type)
        self.assertEqual(review.object_id, movie.id)
        self.assertEqual(review.rating, 5)
        self.assertEqual(review.comment, "Great movie!")
        self.assertTrue(review.date_added)
        self.assertTrue(review.date_modified)
        self.assertTrue(review.id)
        film = review.content_type.get_object_for_this_type(
            id=review.object_id
        )
        self.assertEqual(
            str(review), f"{film.title} ({review.rating})"
        )
