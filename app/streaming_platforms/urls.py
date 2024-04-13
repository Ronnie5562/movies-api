"""
Urls for the streaming_platforms app.
"""
from django.urls import path
from streaming_platforms.views import PlatformListView, PlatformRetrieveView


app_name = 'streaming_platforms'

urlpatterns = [
    path('', PlatformListView.as_view(), name='platform-list'),
    path('<int:id>', PlatformRetrieveView.as_view(), name='platform-detail'),
]
