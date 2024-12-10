from django import forms
from django.views import View
from django.shortcuts import render, redirect
from datetime import date

from django.contrib.auth.mixins import LoginRequiredMixin

from todolist_dtos.models.dayplan import DayPlan
from todolist_dtos.services.dayplan_service import DayPlanService
from todolist_dtos.repositories.dayplan_repository import DayPlanRepository

from tasks.forms import ChoiceDayForm

class ChoiceDayPlanView(LoginRequiredMixin, View):

    def get(self, request):
        form = ChoiceDayForm(initial={'choice_day': date.today()})
        context = {
            'form': form
        }
        return render(request, 'tasks/choice_day.html', context=context)

    def post(self, request):
        date_b = [int(i) for i in request.POST['choice_day'].split('-')]
        form = ChoiceDayForm(request.POST)
        if DayPlanService(DayPlanRepository()).is_exists(request.user.username, date_b):
            dayplan = DayPlanService(DayPlanRepository()).get_day(request.user.username, date_b)
            return redirect(dayplan)
        else:
            return render(request,'tasks/choice_day.html',context={'form':form, 'info':f"Такой даты нет"})

