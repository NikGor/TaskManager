from django.contrib import admin
from .models import Task
from ..labels.models import Label


class LabelInline(admin.StackedInline):
    model = Label.tasks.through


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'status', 'priority', 'project', 'is_closed')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'description')
    list_filter = ('status', 'project', 'priority', 'is_closed')
    empty_value_display = '-пусто-'
    list_editable = ('status', 'priority', 'is_closed')
    save_on_top = True
