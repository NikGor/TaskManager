from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    # Добавить дополнительные поля в list_display
    list_display = ('username', 'email', 'first_name',
                    'last_name', 'is_staff', 'is_active',
                    'last_login', 'date_joined')

    # Добавить фильтры
    list_filter = ('is_staff', 'is_active')

    # Поля только для чтения
    readonly_fields = ('last_login', 'date_joined')

    # Пользовательские действия
    actions = ['make_active', 'make_inactive']

    def make_active(self, request, queryset):
        queryset.update(is_active=True)

    make_active.short_description = "Активировать выбранных пользователей"

    def make_inactive(self, request, queryset):
        queryset.update(is_active=False)

    make_inactive.short_description = "Деактивировать выбранных пользователей"
