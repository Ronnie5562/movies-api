"""
Views for the movies app APIs.
"""
from rest_framework import (
    generics,
    viewsets
)
from movies.models import (
    Genre,
    Movie,
    Season,
    Episode,
    Review
)
from movies.serializers import (
    GenreSerializer,
    MovieSerializer,
    SeasonSerializer,
    EpisodeSerializer,
    ReviewSerializer
)
from movies import permissions as CustomMoviesPermissions


class GenreBaseView(generics.GenericAPIView):
    """
    Base View for Genre model.
    """
    queryset = Genre.objects.all().order_by('-id')
    serializer_class = GenreSerializer
    permission_classes = [CustomMoviesPermissions.IsAdminOrReadOnly]
    lookup_field = 'id'


class GenreListCreateView(generics.ListCreateAPIView,
                          GenreBaseView):
    """
    API View for Genre model.
    """


class GenreDetailView(generics.RetrieveUpdateDestroyAPIView,
                      GenreBaseView):
    """
    API View for Genre model.
    """


class MovieBaseView(generics.GenericAPIView):
    """
    Base View for Movie model.
    """
    queryset = Movie.objects.all().order_by('-id')
    serializer_class = MovieSerializer
    permission_classes = [CustomMoviesPermissions.IsAdminOrReadOnly]
    lookup_field = 'id'


class MovieListCreateView(generics.ListCreateAPIView,
                          MovieBaseView):
    """
    API View for Movie model.
    """


class MovieDetailView(generics.RetrieveUpdateDestroyAPIView,
                      MovieBaseView):
    """
    API View for Movie model.
    """


class SeasonBaseView(generics.GenericAPIView):
    """
    Base View for Season model.
    """
    queryset = Season.objects.all().order_by('-id')
    serializer_class = SeasonSerializer
    permission_classes = [CustomMoviesPermissions.IsAdminOrReadOnly]
    lookup_field = 'id'


class SeasonListCreateView(generics.ListCreateAPIView,
                           SeasonBaseView):
    """
    API View for Season model.
    """


class SeasonDetailView(generics.RetrieveUpdateDestroyAPIView,
                       SeasonBaseView):
    """
    API View for Season model.
    """


class EpisodeBaseView(generics.GenericAPIView):
    """
    Base View for Episode model.
    """
    queryset = Episode.objects.all().order_by('-id')
    serializer_class = EpisodeSerializer
    permission_classes = [CustomMoviesPermissions.IsAdminOrReadOnly]
    lookup_field = 'id'


class EpisodeListCreateView(generics.ListCreateAPIView,
                            EpisodeBaseView):
    """
    API View for Episode model.
    """


class EpisodeDetailView(generics.RetrieveUpdateDestroyAPIView,
                        EpisodeBaseView):
    """
    API View for Episode model.
    """


class ReviewViewSet(viewsets.ModelViewSet):
    """
    API View for Review model.
    """
    queryset = Review.objects.all().order_by('-id')
    serializer_class = ReviewSerializer
    permission_classes = [CustomMoviesPermissions.IsReviewAuthororReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
