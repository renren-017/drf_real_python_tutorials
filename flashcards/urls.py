from django.urls import path

from flashcards.views import CardView, CardDetailView

urlpatterns = [
    path('', CardView.as_view(), name='api-cards'),
    path('<int:pk>/', CardDetailView.as_view(), name='api-card-detail'),
]