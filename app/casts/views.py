"""
Views for the Casts App APIs
"""
from casts.serializers import (
    CastSerializer,
    CastUpdateSerializer,
    AwardSerializer,
    AwardReceivedSerializer,
)
from casts.models import Cast, Award, AwardReceived
from rest_framework import generics, mixins, permissions


# Cast Views
class CastView(generics.GenericAPIView):
    """View for the Casts API"""
    queryset = Cast.objects.all().order_by('-id')
    serializer_class = CastSerializer
    lookup_field = 'id'

    def get_permissions(self):
        if self.request.method not in permissions.SAFE_METHODS:
            return [permissions.IsAdminUser()]
        else:
            return super().get_permissions()


class CastCreateListView(mixins.ListModelMixin,
                         mixins.CreateModelMixin,
                         CastView):
    """View for list of casts"""
    def get(self, request, *args, **kwargs):
        """Get the list of casts"""
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, kwargs):
        """Create a new cast"""
        return self.create(request, *args, **kwargs)


class CastDetailView(mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin,
                     CastView):
    """View for details of a single cast"""
    serializer_class = CastUpdateSerializer

    def get(self, request, *args, **kwargs):
        """Get the details of a single cast"""
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        """Update the details of a single cast"""
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        """Update the details of a single cast"""
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        """Delete a single cast"""
        return self.destroy(request, *args, **kwargs)


# Award Views
class AwardView(generics.GenericAPIView):
    """View for the Awards API"""
    queryset = Award.objects.all().order_by('-id')
    serializer_class = AwardSerializer
    lookup_field = 'id'

    def permissions(self):
        if self.request.method not in permissions.SAFE_METHODS:
            return [permissions.IsAdminUser]
        else:
            return super().get_permissions()


class AwardCreateListView(mixins.ListModelMixin,
                          mixins.CreateModelMixin,
                          AwardView):
    """View create award or get list of awards"""
    def get(self, request, *args, **kwargs):
        """Get the list of awards"""
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        """Create a new award"""
        return self.create(request, *args, **kwargs)


class AwardDetailView(mixins.RetrieveModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.DestroyModelMixin,
                      AwardView):
    """View for details of a single award"""
    def get(self, request, *args, **kwargs):
        """Get the details of a single award"""
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        """Update the details of a single award"""
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        """Partially update the details of a single award"""
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        """Delete a single award"""
        return self.destroy(request, *args, **kwargs)


# AwardReceived Views
class AwardReceivedView(generics.GenericAPIView):
    """View for the Awards Received API"""
    queryset = AwardReceived.objects.all().order_by('-id')
    serializer_class = AwardReceivedSerializer
    lookup_field = 'id'

    def get_permissions(self):
        if self.request.method not in permissions.SAFE_METHODS:
            return [permissions.IsAdminUser]
        else:
            return super().get_permissions()


class AwardReceivedCreateListView(mixins.ListModelMixin,
                                  mixins.CreateModelMixin,
                                  AwardReceivedView):
    """View for list of awards received"""
    def get(self, request, *args, **kwargs):
        """Get the list of awards received"""
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        """Give out an award to an actor or director"""
        return self.create(request, *args, **kwargs)


class AwardReceivedDetailView(mixins.RetrieveModelMixin,
                              mixins.UpdateModelMixin,
                              mixins.DestroyModelMixin,
                              AwardReceivedView):
    """View for details of a single award received"""
    def get(self, request, *args, **kwargs):
        """Get the details of a single award received"""
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        """Update the details of a single award received"""
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        """Update the details of a single award received"""
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        """Delete a single award received"""
        return self.destroy(request, *args, **kwargs)
