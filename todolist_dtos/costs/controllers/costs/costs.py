from django.views import View
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin

from costs.repository import CostRepository
from costs.cost_service import CostService

class CostslistView(LoginRequiredMixin, View):

    def get(self, request):

        context = {
            'costs': CostService(CostRepository()).list_objects()
        }
        return render(request, 'costs/costs_list.html', context=context)