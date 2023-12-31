"""
URL configuration for task_manager project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
from task_manager.views import IndexView, LoginView, LogoutView, SettingsView

urlpatterns = i18n_patterns(
    # Admin
    path("admin/", admin.site.urls),

    # Auth routes
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    # Main routes
    path('', IndexView.as_view(), name='index'),
    path('settings/', SettingsView.as_view(), name='settings'),

    # App-specific routes
    path('users/', include('task_manager.users.urls')),
    path('tasks/', include('task_manager.tasks.urls')),
    path('labels/', include('task_manager.labels.urls')),
    path('projects/', include('task_manager.projects.urls')),
    path('dashboard/', include('task_manager.dashboard.urls')),
)

urlpatterns += [
    path('i18n/', include('django.conf.urls.i18n')),
]
