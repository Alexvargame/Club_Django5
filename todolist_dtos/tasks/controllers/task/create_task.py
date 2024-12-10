from django.views import View
from django.shortcuts import render, redirect

from django.contrib.auth.mixins import LoginRequiredMixin

from tasks.tasks_service import TaskService

from tasks.dtos.request.create_task_dto import CreateTaskDTO
from tasks.repository import TaskRepository
from tasks.forms import TaskForm

class TaskCreateView(LoginRequiredMixin, View):
    def get(self, request):
        form = TaskForm()
        return render(request, 'tasks/task_create.html', {'form': form})

    def post(self, request):
        form = TaskForm(request.POST)
        if form.is_valid():
            data = CreateTaskDTO(
                **form.cleaned_data,
                user=request.user.username
            )
            TaskService(TaskRepository()).create_object(data)
            return redirect('tasks_list_url')


        return redirect('task_create_url')





