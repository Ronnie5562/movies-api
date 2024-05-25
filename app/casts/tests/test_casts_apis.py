from django.urls import reverse
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model
from casts.models import (
    Cast,
    Award,
    AwardReceived
)
from casts.serializers import (
    CastSerializer,
    AwardSerializer,
    AwardReceivedSerializer
)