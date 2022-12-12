from django.contrib import admin

from to_do.models import ToDoItem, ToDoList


class ToDoListAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    search_fields = ('title',)


admin.site.register(ToDoList, ToDoListAdmin)


class ToDoItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'created_date', 'due_date', 'todo_list')
    list_filter = ('todo_list',)


admin.site.register(ToDoItem, ToDoItemAdmin)
