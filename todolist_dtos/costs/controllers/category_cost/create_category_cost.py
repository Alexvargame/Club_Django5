from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin


from todolist_dtos.services.category_cost_service import CategoryCostService
from todolist_dtos.repositories.category_cost_repository import CategoryCostRepository

from costs.dtos.request.category_cost_create_dto import CategoryCostCreateDTO
from costs.forms import CategoryCostForm

class CategoryCostCreateView(LoginRequiredMixin, View):

    def get(self, request):
        form = CategoryCostForm()
        context = {
            'form': form,
        }
        return render(request, 'costs/category_cost_create.html', context=context)

    def post(self, request):
        b_form = CategoryCostForm(request.POST)
        if b_form.is_valid():
            dto = CategoryCostCreateDTO(
                **b_form.cleaned_data
            )
            CategoryCostService(CategoryCostRepository()).create_object(dto)

            return redirect('category_costs_list_url')
        context = {
            'form': form,
        }
        return render(request, 'costs/category_cost_create.html', context=context)