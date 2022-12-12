from django.urls import path

from projects.views import ProjectView, ProjectDetailView

urlpatterns = [
    path('', ProjectView.as_view(), name='api-projects'),
    path('<int:pk>/', ProjectDetailView.as_view(), name='api-project-detail'),
]
