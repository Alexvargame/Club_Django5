from django import forms
from django.views import View
from django.shortcuts import render, redirect
from datetime import date

from django.contrib.auth.mixins import LoginRequiredMixin

from todolist_dtos.models.dayplan import DayPlan
from todolist_dtos.services.dayplan_service import DayPlanService
from todolist_dtos.repositories.dayplan_repository import DayPlanRepository

from tasks.forms import CreateDayTasksForm
from tasks.repository import TaskRepository
from tasks.tasks_service import TaskService
from tasks.dtos.request.create_dayplan_dto import CreateDayPlanDTO

class DayPlanUpdate(LoginRequiredMixin, View):

    def get(self, request, user, year, month, day):

        dayplan = DayPlan.objects.get(user=request.user.username, day_date__year=year,
                                      day_date__month=month, day_date__day=day)
        tasks = TaskService(TaskRepository()).list_for_day_plan(request.user.username, False, date.today(), date(2025,1, 1))

        form = CreateDayTasksForm()
        context = {
            'dayplan' : dayplan,
            'tasks': form['tasks'].as_widget(forms.CheckboxSelectMultiple(choices=[(t.name, t.name) for t in tasks if t not in dayplan.tasks.all() ]))
        }

        return render(request, 'tasks/update_day.html', context=context)

    def post(self, request, user, year, month, day):
        dayplan = DayPlan.objects.get(user=request.user.username, day_date__year=year,
                                      day_date__month=month, day_date__day=day)
        bound_form = CreateDayTasksForm(request.POST)
        tasks = list(TaskService(TaskRepository()).list_for_day_plan(request.user.username, False, date.today(),
                                                                date(2025, 1, 1)))
        update_tasks = list(TaskService(TaskRepository()).get_choices_tasks(bound_form.data.getlist('tasks')))
        tasks.extend(update_tasks)
        if bound_form.is_valid():
            data = CreateDayPlanDTO(
                user=request.user.username,
                day_date=dayplan.day_date,
                tasks=tasks,
            )
            DayPlanService(DayPlanRepository()).update_object(data)
            return redirect(dayplan)

        context = {
            'dayplan': dayplan,
            'tasks': form['tasks'].as_widget(
                forms.CheckboxSelectMultiple(choices=[(t.name, t.name) for t in tasks if t not in dayplan.tasks.all()]))
        }

        return render(request, 'tasks/update_day.html', context=context)