from django.views import View
from django.shortcuts import render, redirect

from django.contrib.auth.mixins import LoginRequiredMixin

from tasks.tasks_service import TaskService

from tasks.dtos.response.task_dto import TaskDTO
from tasks.repository import TaskRepository

from todolist_dtos.models.task import Task

class TaskDetailView(LoginRequiredMixin, View):
    def get(self, request, pk):
        obj = Task.objects.get(id=pk)
        dto = TaskService(TaskRepository()).detail_object(obj)
        context = {'task': dto.__dict__}
        return render(request, 'tasks/task_detail.html', context=context)






