"""
Views for the user API.
"""
from django.contrib.auth import get_user_model
from rest_framework.settings import api_settings
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework import generics, authentication, permissions
from users.serializers import UserSerializer, AuthTokenSerializer


class CreateUserView(generics.CreateAPIView):
    """
    Create a new user in the system.
    """
    serializer_class = UserSerializer


class UsersListView(generics.ListAPIView):
    """
    List of users in the system.
    """
    serializer_class = UserSerializer
    queryset = get_user_model().objects.all()
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]


class ManageUserView(generics.RetrieveUpdateAPIView):
    """
    Manage the authenticated user.
    """
    serializer_class = UserSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        """
        Retrieve and return the authenticated user
        """
        return self.request.user


class CreateTokenView(ObtainAuthToken):
    """
    Create a new auth token for user
    """
    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
