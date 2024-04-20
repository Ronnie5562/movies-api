"""
Serializers for the movies app.
"""
from rest_framework import serializers
from movies.models import (
    Genre,
    Movie,
    Season,
    Episode,
    Review
)
from streaming_platforms.serializers import PlatformSerializer


class GenreSerializer(serializers.ModelSerializer):
    """
    Serializer for the Genre model.
    """
    class Meta:
        model = Genre
        fields = ['id', 'name', 'description', 'is_active']
        read_only_fields = ['id']


class MovieSerializer(serializers.ModelSerializer):
    """
    Serializer for the Movie model.
    """
    genres = GenreSerializer(many=True, required=False)
    platform = PlatformSerializer(required=False)
    actors = serializers.StringRelatedField(many=True, required=False)
    starring = serializers.StringRelatedField(many=True, required=False)
    directors = serializers.StringRelatedField(many=True, required=False)

    url = serializers.CharField(source="get_absolute_url", read_only=True)

    class Meta:
        model = Movie
        exclude = ['date_added', 'date_modified']
        read_only_fields = [
            'id', 'avg_rating', 'rating_count',
            'popularity', 'views', 'reviews'
        ]


class SeasonSerializer(serializers.ModelSerializer):
    """
    Serializer for the Season model.
    """
    url = serializers.CharField(source="get_absolute_url", read_only=True)

    class Meta:
        model = Season
        exclude = ['date_added', 'date_modified']
        read_only_fields = [
            'id', 'avg_rating', 'rating_count',
            'popularity', 'views', 'reviews'
        ]


class EpisodeSerializer(serializers.ModelSerializer):
    """
    Serializer for the Episode model.
    """
    url = serializers.CharField(source="get_absolute_url", read_only=True)

    class Meta:
        model = Episode
        exclude = ['date_added', 'date_modified']
        read_only_fields = [
            'id', 'avg_rating', 'rating_count',
            'popularity', 'views', 'reviews',
        ]


class ReviewSerializer(serializers.ModelSerializer):
    """
    Serializer for the Review model.
    """
    url = serializers.CharField(source="get_absolute_url", read_only=True)

    class Meta:
        model = Review
        exclude = ['date_added', 'date_modified']
        read_only_fields = ['id', 'content']
        write_only_fields = ['content_type', 'object_id']
