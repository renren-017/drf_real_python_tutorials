from django.contrib import admin

from flashcards.models import Card


class CardAdmin(admin.ModelAdmin):
    list_display = ('id', 'question', 'answer', 'box', 'date_created')
    list_filter = ('box', )
    ordering = ('-date_created',)


admin.site.register(Card, CardAdmin)
