from django.views import View
from django.shortcuts import render, redirect

from django.contrib.auth.mixins import LoginRequiredMixin

from tasks.tasks_service import TaskService

from tasks.dtos.response.task_dto import TaskDTO
from tasks.repository import TaskRepository
from tasks.forms import TaskForm
from todolist_dtos.models.task import Task

class TaskUpdateView(LoginRequiredMixin, View):
    def get(self, request, pk):
        task = Task.objects.get(id=pk)
        form = TaskForm(instance=task)
        return render(request, 'tasks/task_update.html', {'form': form})

    def post(self, request, pk):
        task = Task.objects.get(id=pk)
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            data = TaskDTO(
                **form.cleaned_data,
                user=request.user.username,
                id=task.id,
            )
            TaskService(TaskRepository()).update_object(data)
            return redirect('tasks_list_url')
        return redirect('task_update_url')





