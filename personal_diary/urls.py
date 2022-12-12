from django.urls import path

from personal_diary.views import EntryView, EntryDetailView

urlpatterns = [
    path('', EntryView.as_view(), name='api-entries'),
    path('<int:pk>/', EntryDetailView.as_view(), name='api-entry-detail'),
]