from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('profile/', TemplateView.as_view(), name='profile')
]
