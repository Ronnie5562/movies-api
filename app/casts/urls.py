"""
Url mappings for the casts App APIs.
"""
from django.urls import path
from casts.views import (
    CastCreateListView,
    CastDetailView,
    AwardCreateListView,
    AwardDetailView,
    AwardReceivedCreateListView,
    AwardReceivedDetailView
)

urlpatterns = [
    path("", CastCreateListView.as_view(), name="casts"),
    path("<int:id>/", CastDetailView.as_view(), name="cast-detail"),
    path("awards/", AwardCreateListView.as_view(), name="awards"),
    path("awards/<int:id>/", AwardDetailView.as_view(), name="award-detail"),
    path(
        "awards-received/",
        AwardReceivedCreateListView.as_view(),
        name="award-received"
    ),
    path(
        "awards-received/<int:id>/",
        AwardReceivedDetailView.as_view(),
        name="award-received-detail"
    )
]
