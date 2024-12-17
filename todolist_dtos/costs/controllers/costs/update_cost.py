from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from decimal import Decimal

from django.contrib.auth.models import User

from costs.repository import CostRepository
from costs.cost_service import CostService
from costs.dtos.response.cost_dto import CostDTO
from costs.forms import CostCreateForm

from todolist_dtos.models.cost import Cost

class CostUpdateView(LoginRequiredMixin, View):

    def get(self, request, pk):
        cost = Cost.objects.get(id=pk)
        form = CostCreateForm(instance=cost)

        context = {
            'form': form,
            'cost': cost,
        }
        return render(request, 'costs/cost_update.html', context=context)

    def post(self, request, pk):
        cost = Cost.objects.get(id=pk)
        b_form = CostCreateForm(request.POST)
        user = cost.user
        old_balance = user.profile.balance
        old_cost_sum = cost.cost_sum
        if b_form.is_valid():
            dto = CostDTO(
                **b_form.cleaned_data,
                id=pk,
            )
            CostService(CostRepository()).update_object(dto)
            user.profile.balance = user.profile.balance + old_cost_sum - Decimal(b_form['cost_sum'].value())
            user.profile.save()
            return redirect('costs_list_url')


        context = {
            'form': b_form,
            'cost': cost,
        }
        return render(request, 'costs/cost_update.html', context=context)