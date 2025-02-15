from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin

from todolist_dtos.models.day_cost import DayCost
from costs.dtos.response.day_cost_dto import DayCostDTO

from todolist_dtos.services.day_cost_service import DayCostService
from todolist_dtos.repositories.day_cost_repository import DayCostRepository

class DayCostDetailView(LoginRequiredMixin, View):

    def get(self, request, year, month, day, user):
        daycost = DayCost.objects.get(user=request.user.username,day_date__year=year,
                                       day_date__month=month,day_date__day=day)
        dto = DayCostService(DayCostRepository()).detail_object(daycost)

        context = {
            'daycost': dto.__dict__,
            'user': dto.user
        }
        return render(request, 'costs/day_cost_detail.html', context=context)