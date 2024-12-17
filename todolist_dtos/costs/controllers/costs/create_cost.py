from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User

from costs.repository import CostRepository
from costs.cost_service import CostService

from costs.dtos.request.cost_create_dto import CostCreateDTO
from costs.forms import CostCreateForm

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
            return redirect('costs_list_url')
        context = {
            'form': b_form,
        }
        return render(request, 'costs/cost_create.html', context=context)
