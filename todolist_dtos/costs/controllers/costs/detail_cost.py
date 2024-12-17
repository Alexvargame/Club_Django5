from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin

from todolist_dtos.models.cost import Cost

from costs.repository import CostRepository
from costs.cost_service import CostService


class CostDetailView(LoginRequiredMixin, View):

    def get(self, request, pk):
        cost = Cost.objects.get(id=pk)
        dto = CostService(CostRepository()).detail_object(cost)
        context = {
            'cost': dto.__dict__
        }
        return render(request, 'costs/cost_detail.html', context=context)