from django.views import View
from django.shortcuts import render, redirect, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from decimal import Decimal

from django.contrib.auth.models import User

from costs.repository import CostRepository
from costs.cost_service import CostService
from costs.dtos.response.cost_dto import CostDTO

from todolist_dtos.models.cost import Cost

class CostDeleteview(LoginRequiredMixin, View):

    def get(self, request, pk):
        cost = Cost.objects.get(id=pk)
        context = {
            'cost': cost
        }
        return render(request, 'costs/cost_delete.html', context=context)

    def post(self, request, pk):
        cost = Cost.objects.get(id=pk)
        dto = CostDTO(
            id=cost.id,
            user=cost.user,
            category=cost.category,
            cost_name=cost.cost_name,
            cost_sum=cost.cost_sum,
            cost_date=cost.cost_date,
        )

        CostService(CostRepository()).delete_object(dto)
        user = cost.user
        user.profile.balance += Decimal(dto.cost_sum)
        user.profile.save()
        return redirect('costs_list_url')