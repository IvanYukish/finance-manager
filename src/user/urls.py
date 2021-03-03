from django.urls import path, include

from user.views import ProfileDetailView, ProfileUpdateView, UserListView

urlpatterns = [
    path('', include('allauth.urls')),
    path('profile/', ProfileDetailView.as_view(), name='profile'),
    path('profile/update', ProfileUpdateView.as_view(), name='profile-update'),

    path('list/', UserListView.as_view(), name='user-list'),
]
