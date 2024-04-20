"""
URL mappings for the movies App APIs.
"""
from movies.views import (
    GenreListCreateView,
    GenreDetailView,
    MovieListCreateView,
    MovieDetailView,
    SeasonListCreateView,
    SeasonDetailView,
    EpisodeListCreateView,
    EpisodeDetailView,
    ReviewViewSet
)
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"reviews", ReviewViewSet, basename="review")

urlpatterns = [
    path("", MovieListCreateView.as_view(), name="movies"),
    path("<int:id>/", MovieDetailView.as_view(), name="movie"),
    path("seasons/", SeasonListCreateView.as_view(), name="seasons"),
    path("seasons/<int:id>/", SeasonDetailView.as_view(), name="season"),
    path("episodes/", EpisodeListCreateView.as_view(), name="episodes"),
    path("episodes/<int:id>/", EpisodeDetailView.as_view(), name="episode"),
    path("genres/", GenreListCreateView.as_view(), name="genres"),
    path("genres/<int:id>/", GenreDetailView.as_view(), name="genre"),
    path("", include(router.urls)),
]
