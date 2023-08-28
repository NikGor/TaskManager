from django.contrib import admin
from .models import Priority


# Register your models here.
@admin.register(Priority)
class PriorityAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'order')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_editable = ('order',)
    save_on_top = True
