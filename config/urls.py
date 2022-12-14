from django.contrib import admin
from django.urls import path, re_path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version='v1',
        description="Test description",
    ),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('projects/', include('projects.urls')),
    path('blogs/', include('blogs.urls')),
    path('todo/', include('to_do.urls')),
    path('entries/', include('personal_diary.urls')),
    path('flashcards/', include('flashcards.urls')),
    path('podcasts/', include('content_aggregator.urls')),

    path('api-auth/', include('rest_framework.urls')),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
