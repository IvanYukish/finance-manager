from allauth.account.views import LoginView
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('', include('allauth.urls')),
    path('profile/', TemplateView.as_view(), name='profile'),
]
