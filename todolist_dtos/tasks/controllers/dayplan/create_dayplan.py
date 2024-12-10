from django import forms
from django.views import View
from django.shortcuts import render, redirect
from datetime import date

from django.contrib.auth.mixins import LoginRequiredMixin

from todolist_dtos.models.task import Task
from todolist_dtos.repositories.dayplan_repository import DayPlanRepository
from todolist_dtos.services.dayplan_service import DayPlanService

from tasks.tasks_service import TaskService
from tasks.dtos.request.create_dayplan_dto import CreateDayPlanDTO
from tasks.repository import TaskRepository

from tasks.forms import CreateDayTasksForm, CreateDayForm

class DayPlanCreateView(LoginRequiredMixin, View):
    def get(self, request):
        print('CREATE DAYPLAN')
        form = CreateDayForm(initial={'user': request.user.username})
        form_tasks = CreateDayTasksForm()
        tasks = TaskService(TaskRepository()).list_for_day_plan(request.user.username, False, date.today(), date(2025,1,1))
        context = {
            'form': form,
            'form_tasks': form_tasks,
            #'tasks': form_tasks['tasks'].as_widget(forms.CheckboxSelectMultiple(choices=[(t.id, t.name) for t in Task.objects.filter(user=request.user.username,status=False,date_to_do__range=(date.today(), date(2025,1,1)))]))}
            'tasks': form_tasks['tasks'].as_widget(forms.CheckboxSelectMultiple(choices=[(t.name, t.name) for t in tasks]))
        }
        return render(request, 'tasks/create_day.html', context=context)

    def post(self, request):

        bound_form = CreateDayForm(request.POST, initial={'user': request.user.username})
        bound_form_tasks = CreateDayTasksForm(request.POST)

        date_b = [int(i) for i in request.POST['day_date'].split('-')]
        # tasks = TaskService(TaskRepository()).get_choices_tasks(bound_form_tasks['tasks'].value())
        # print('value task', tasks)

        if DayPlanService(DayPlanRepository()).is_exists(request.user.username, date_b):
            day = DayPlanService(DayPlanRepository()).get_day(request.user.username, date_b)

            return redirect(day)
        if bound_form.is_valid() and bound_form_tasks.is_valid():
            data = CreateDayPlanDTO(
                **bound_form.cleaned_data,
                user=request.user.username,
                tasks=list(TaskService(TaskRepository()).get_choices_tasks(bound_form_tasks.data.getlist('tasks'))),
            )
            DayPlanService(DayPlanRepository()).create_object(data)
            return redirect('tasks_list_url')
        #list(CityRepository().filter_cities(data.getlist('cities')))
        return redirect('dayplan_create_url')



