from django.urls import path

from content_aggregator.views import EpisodeView

urlpatterns = [
    path('', EpisodeView.as_view(), name='api-episodes'),
]