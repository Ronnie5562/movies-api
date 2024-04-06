"""
URL mapping for users API.
"""

from django.urls import path
from users import views

app_name = 'users'

urlpatterns = [
    path('me/', views.ManageUserView.as_view(), name='me'),
    path('token/', views.CreateTokenView.as_view(), name='token'),
    path('create/', views.CreateUserView.as_view(), name='create'),
    path('list/', views.UsersListView.as_view(), name='list')
]
