"""
Urls for the streaming_platforms app.
"""
from django.urls import path
from streaming_platforms.views import PlatformsView


app_name = 'streaming_platforms'

urlpatterns = [
    path('', PlatformsView.as_view(), name='platform-list'),
    path('<int:id>', PlatformsView.as_view(), name='platform-detail'),
]
