from django.shortcuts import render
from task_manager.tasks.models import Task
from task_manager.projects.models import Project


def dashboard_view(request):
    # Общие данные
    total_tasks = Task.objects.count()
    total_open_tasks = Task.objects.exclude(status__name="завершена").count()

    # Данные по проектам
    projects_data = []
    for project in Project.objects.all():
        project_tasks = Task.objects.filter(project=project)
        project_open_tasks = project_tasks.exclude(status__name="завершена")
        projects_data.append({
            'project_name': project.name,
            'total_tasks': project_tasks.count(),
            'open_tasks': project_open_tasks.count(),
        })

    context = {
        'total_tasks': total_tasks,
        'total_open_tasks': total_open_tasks,
        'projects': projects_data,
    }

    return render(request, 'task_manager/dashboard.html', context)
