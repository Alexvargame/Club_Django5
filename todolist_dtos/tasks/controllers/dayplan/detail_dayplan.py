from django.views import View
from django.shortcuts import render, redirect

from django.contrib.auth.mixins import LoginRequiredMixin

from tasks.dtos.response.dayplan_dto import DayPlanDTO

from todolist_dtos.repositories.dayplan_repository import DayPlanRepository
from todolist_dtos.services.dayplan_service import DayPlanService

from todolist_dtos.models.dayplan import DayPlan

class DayPlanDetailView(LoginRequiredMixin, View):
    def get(self, request, user, year, month, day):
        obj = DayPlan.objects.get(user=request.user.username, day_date__year=year, day_date__month=month, day_date__day=day)
        dto = DayPlanService(DayPlanRepository()).detail_object(obj)
        context = {'day': dto.__dict__}
        return render(request, 'tasks/day_detail.html', context=context)






