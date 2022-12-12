from django.contrib import admin

from content_aggregator.models import Episode


class EpisodeAdmin(admin.ModelAdmin):
    list_display = ('id', 'image', 'description', 'link', 'podcast_name', 'pub_date', 'guid')
    list_filter = ('podcast_name',)
    ordering = ('-pub_date',)


admin.site.register(Episode, EpisodeAdmin)
