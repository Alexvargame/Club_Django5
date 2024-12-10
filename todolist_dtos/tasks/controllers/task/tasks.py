from django.views import View
from django.shortcuts import render

from tasks.tasks_service import TaskService
from tasks.repository import TaskRepository

class TasksListvew(View):

    def get(self, request):
        context = {
            'tasks': TaskService(TaskRepository()).list_objects
        }
        return render(request, 'tasks/tasks_list.html', context=context)