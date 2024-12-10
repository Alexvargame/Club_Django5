from django.views import View
from django.shortcuts import render, redirect

from django.contrib.auth.mixins import LoginRequiredMixin

from tasks.tasks_service import TaskService
from todolist_dtos.models.task import Task

from tasks.dtos.response.task_dto import TaskDTO
from tasks.repository import TaskRepository

class TaskDeleteView(LoginRequiredMixin, View):
    def get(self, request, pk):
        task = Task.objects.get(id=pk)
        context = {'task': task}
        return render(request, 'tasks/task_delete.html', context=context)

    def post(self, request,pk):
        task = Task.objects.get(id=pk)
        task.__dict__.pop('_state')
        data = TaskDTO(**task.__dict__)
        TaskService(TaskRepository()).delete_object(data)
        return redirect('tasks_list_url')





