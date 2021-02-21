from django.urls import path, include

from user.views import ProfileDetailView

urlpatterns = [
    path('', include('allauth.urls')),
    path('profile/', ProfileDetailView.as_view(), name='profile'),
]
