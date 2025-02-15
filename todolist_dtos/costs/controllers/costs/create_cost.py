from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User

from costs.repository import CostRepository
from costs.cost_service import CostService
from costs.dtos.request.cost_create_dto import CostCreateDTO
from costs.forms import CostCreateForm

from todolist_dtos.models.day_cost import DayCost
from todolist_dtos.models.cost import Cost
class CostCreateView(LoginRequiredMixin, View):

    def get(self, request):

        form = CostCreateForm()
        context = {
            'form': form,
        }
        return render(request, 'costs/cost_create.html', context=context)

    def post(self, request):

        b_form = CostCreateForm(request.POST)
        user = User.objects.get(id=b_form['user'].value())
        if b_form.is_valid():
            dto = CostCreateDTO(
                **b_form.cleaned_data
            )
            CostService(CostRepository()).create_object(dto)

            user.profile.balance -= dto.cost_sum
            user.profile.save()
            cost_date = b_form['cost_date'].value()
            if DayCost.objects.filter(day_date=cost_date).exists():
                day = DayCost.objects.get(day_date=cost_date)
                cost_d = Cost.objects.filter(cost_date=cost_date, user=user)
                day.costs.set(cost_d)
                day.save()
            else:
                day = DayCost.objects.create(user=request.user.username, day_date=cost_date)
                cost_d = Cost.objects.filter(cost_date=cost_date, user=user)
                day.costs.set(cost_d)
                day.save()
            return redirect('costs_list_url')
        context = {
            'form': b_form,
        }
        return render(request, 'costs/cost_create.html', context=context)
