"""
Stream Platforms API Serializers
"""
from rest_framework import serializers
from streaming_platforms.models import Platform


class PlatformSerializer(serializers.ModelSerializer):
    """
    Serializer for the Stream Platform object
    """
    class Meta:
        model = Platform
        fields = ["id", "name", "website", "about"]
        read_only_fields = ['id']
