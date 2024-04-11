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


class PlatformsView(
                    mixins.ListModelMixin,
                    mixins.RetrieveModelMixin,
                    generics.GenericAPIView):
    """
    List all streaming platforms or retrieve a single platform.
    """
    queryset = Platform.objects.all().order_by('-id')
    serializer_class = PlatformSerializer
    lookup_field = 'id'
    throttle_classes = [UserPlatformViewThrottle, AnonPlatformViewThrottle]

    def get(self, request, *args, **kwargs):
        """
        Get the either the streaming platforms list \
        or a single streaming platform
        """
        if kwargs.get('id'):
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)
