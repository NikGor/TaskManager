import django_filters
from task_manager.tasks.models import Task


class TaskFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    label = django_filters.NumberFilter(method='filter_label')
    is_closed = django_filters.BooleanFilter(method='filter_is_closed')

    class Meta:
        model = Task
        fields = ['name', 'status', 'priority', 'executor', 'label', 'project', 'is_closed']

    def filter_label(self, queryset, name, value):
        return queryset.filter(labels__in=[value])
