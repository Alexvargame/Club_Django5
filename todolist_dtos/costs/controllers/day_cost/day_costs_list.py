from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin



from todolist_dtos.services.day_cost_service import DayCostService
from todolist_dtos.repositories.day_cost_repository import DayCostRepository

class DayCostsListView(LoginRequiredMixin, View):

    def get(self, request):

        context = {
            'daycosts' : DayCostService(DayCostRepository()).list_objects()
        }
        return render(request, 'costs/day_cost_list.html', context=context)