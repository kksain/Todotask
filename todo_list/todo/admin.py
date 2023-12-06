from django.contrib import admin
from .models import TodoItem, Tag


class TodoItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'timestamp', 'due_date', 'status')
    list_filter = ('status', 'due_date')
    search_fields = ('title', 'description')


admin.site.register(TodoItem, TodoItemAdmin)
admin.site.register(Tag)
