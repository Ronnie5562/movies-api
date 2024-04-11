"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView
)

urlpatterns = [
    # Admin page
    path('admin/', admin.site.urls),

    # Apps
    path('api/v1/users/', include('users.urls')),
    path('api/v1/platforms/', include('streaming_platforms.urls')),

    # API documentation
    path(
        'api/v1/schema/',
        SpectacularAPIView.as_view(),
        name='api-schema'
    ),
    path(
        'api/v1/docs/',
        SpectacularSwaggerView.as_view(url_name='api-schema'),
        name='api-docs'
    ),
    path(
        'api/v1/redoc-docs/',
        SpectacularRedocView.as_view(url_name='api-schema'),
        name='api-redoc-docs'
    ),
]
