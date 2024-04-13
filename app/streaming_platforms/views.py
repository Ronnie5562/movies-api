"""
Views for the streaming platform API.
"""
from rest_framework import generics, mixins
from streaming_platforms.throttling import (
    UserPlatformViewThrottle,
    AnonPlatformViewThrottle
)
from streaming_platforms.models import Platform
from streaming_platforms.serializers import PlatformSerializer


class PlatformsView(generics.GenericAPIView):
    """
    List all streaming platforms or retrieve a single platform.
    """
    queryset = Platform.objects.all().order_by('-id')
    serializer_class = PlatformSerializer
    lookup_field = 'id'
    throttle_classes = [AnonPlatformViewThrottle, UserPlatformViewThrottle]


class PlatformListView(mixins.ListModelMixin, PlatformsView):
    """
    List all streaming platforms.
    """
    def get(self, request, *args, **kwargs):
        """
        Get the streaming platforms list
        """
        return self.list(request, *args, **kwargs)


class PlatformRetrieveView(mixins.RetrieveModelMixin, PlatformsView):
    """
    Retrieve a single streaming platform.
    """
    def get(self, request, *args, **kwargs):
        """
        Get a single streaming platform
        """
        return self.retrieve(request, *args, **kwargs)
