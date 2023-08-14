from django.shortcuts import redirect
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from task_manager.mixins import CustomLoginRequiredMixin
from .models import Project
from .forms import ProjectForm
from django.utils.translation import gettext as _


class ProjectListView(CustomLoginRequiredMixin, ListView):
    model = Project
    template_name = 'projects/projects.html'
    context_object_name = 'projects'


class ProjectCreateView(CustomLoginRequiredMixin, CreateView):
    model = Project
    form_class = ProjectForm
    template_name = 'projects/project_create.html'
    success_url = reverse_lazy('projects:projects_list')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        messages.success(self.request, _('Проект успешно создан'))
        return super().form_valid(form)


class ProjectUpdateView(CustomLoginRequiredMixin, UpdateView):
    model = Project
    form_class = ProjectForm
    template_name = 'projects/project_update.html'
    success_url = reverse_lazy('projects:projects_list')

    def form_valid(self, form):
        messages.success(self.request, _('Проект успешно обновлен'))
        return super().form_valid(form)


class ProjectDeleteView(CustomLoginRequiredMixin, DeleteView):
    model = Project
    template_name = 'projects/project_delete.html'
    success_url = reverse_lazy('projects:projects_list')

    def form_valid(self, form):
        self.object = self.get_object()
        if self.object.task_set.exists():
            messages.error(self.request, _('Невозможно удалить проект, связанный с задачами.'))
            return redirect('projects:projects_list')
        self.object.__class__.objects.filter(id=self.object.id).delete()
        messages.success(self.request, _('Проект успешно удален'))
        return super().form_valid(form)
