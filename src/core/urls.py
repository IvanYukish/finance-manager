from django.urls import path, include

from core.views import HomeView

urlpatterns = [
    path('', HomeView.as_view(), name='home')

]
