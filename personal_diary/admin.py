from django.contrib import admin

from personal_diary.models import Entry


class EntryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'date_created')
    ordering = ('-date_created',)


admin.site.register(Entry, EntryAdmin)
