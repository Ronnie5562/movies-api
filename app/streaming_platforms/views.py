"""
Views for the streaming platform API.
"""
from rest_framework import generics, mixins, permissions, authentication
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
    authentication_classes = [authentication.TokenAuthentication]
    throttle_classes = [AnonPlatformViewThrottle,
                        UserPlatformViewThrottle]

    def get_permissions(self):
        if self.request.method not in permissions.SAFE_METHODS:
            return [permissions.IsAdminUser()]
        else:
            return super().get_permissions()


class PlatformListView(mixins.ListModelMixin,
                       mixins.CreateModelMixin,
                       PlatformsView):
    """
    ListCreate View for the streaming platforms.
    """
    def get(self, request, *args, **kwargs):
        """Get the streaming platforms list"""
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        """Create a new platform in the system"""
        return self.create(request, *args, **kwargs)


class PlatformRetrieveView(mixins.RetrieveModelMixin,
                           mixins.UpdateModelMixin,
                           mixins.DestroyModelMixin,
                           PlatformsView):
    """
    Retrieve a single streaming platform.
    """
    def get(self, request, *args, **kwargs):
        """Get a single streaming platform"""
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        """Update the details of a single platform"""
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        """Update the details of a single platform"""
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        """Delete a single platform"""
        return self.destroy(request, *args, **kwargs)
