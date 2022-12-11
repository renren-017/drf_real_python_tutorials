from django.urls import path

from projects.views import ProjectView, ProjectDetailView

urlpatterns = [
    path('projects/', ProjectView.as_view(), name='api-projects'),
    path('projects/<int:pk>', ProjectDetailView.as_view(), name='api-project-detail'),
]
