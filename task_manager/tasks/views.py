from django.shortcuts import redirect
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.urls import reverse_lazy
from django_filters.views import FilterView
from task_manager.mixins import CustomLoginRequiredMixin
from .filters import TaskFilter
from .forms import TaskForm, FilterForm
from .models import Task
from task_manager.statuses.models import Status
from task_manager.users.models import User
from task_manager.labels.models import Label
from django.contrib import messages
from django.utils.translation import gettext as _
from django.views.generic import DetailView
from task_manager.priorities.models import Priority
from task_manager.projects.models import Project


class TaskDetailView(CustomLoginRequiredMixin, DetailView):
    model = Task
    template_name = 'tasks/task_detail.html'


class TaskListView(CustomLoginRequiredMixin, FilterView):
    model = Task
    template_name = 'tasks/tasks.html'
    context_object_name = 'tasks'
    filterset_class = TaskFilter

    def get_filterset_kwargs(self, filterset_class):
        kwargs = super().get_filterset_kwargs(filterset_class)
        kwargs.update({'request': self.request})
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = FilterForm(self.request.GET)
        context['statuses'] = Status.objects.all()
        context['priorities'] = Priority.objects.all()
        context['users'] = User.objects.all()
        context['labels'] = Label.objects.all()
        context['projects'] = Project.objects.all()
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        filterset = self.filterset_class(self.request.GET, queryset=queryset)
        queryset = filterset.qs
        is_closed = self.request.GET.get('is_closed', None)
        if is_closed == 'on':
            queryset = queryset.filter(is_closed=False)
        return queryset


class TaskCreateView(CustomLoginRequiredMixin, CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/task_create.html'
    success_url = reverse_lazy('tasks:tasks_list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request, _('Задача успешно создана'))
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = FilterForm(self.request.GET)
        context['statuses'] = Status.objects.all()
        context['priorities'] = Priority.objects.all()
        context['users'] = User.objects.all()
        context['labels'] = Label.objects.all()
        context['projects'] = Project.objects.all()
        return context


class TaskUpdateView(CustomLoginRequiredMixin, UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/task_update.html'
    success_url = reverse_lazy('tasks:tasks_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['statuses'] = Status.objects.all()
        context['priorities'] = Priority.objects.all()
        context['labels'] = Label.objects.all()
        context['users'] = User.objects.all()
        context['projects'] = Project.objects.all()
        return context

    def form_valid(self, form):
        task = form.instance
        if task.status.order in [0, 1]:
            task.is_closed = True
            task.save()
        messages.success(self.request, _('Задача успешно изменена'))
        return super().form_valid(form)


class TaskDeleteView(CustomLoginRequiredMixin, DeleteView):
    model = Task
    template_name = 'tasks/task_delete.html'
    success_url = reverse_lazy('tasks:tasks_list')

    def form_valid(self, form):
        task = self.get_object()
        if task.author != self.request.user:
            messages.error(self.request, _('Вы не можете удалить эту задачу'))
            return redirect('tasks:tasks_list')
        messages.success(self.request, _('Задача успешно удалена'))
        return super().form_valid(form)
