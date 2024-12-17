from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin


from todolist_dtos.services.category_cost_service import CategoryCostService
from todolist_dtos.repositories.category_cost_repository import CategoryCostRepository
from todolist_dtos.models.category_cost import CategoryCost

from costs.dtos.response.category_cost_dto import CategoryCostDTO
from costs.forms import CategoryCostForm

class CategoryCostUpdateView(LoginRequiredMixin, View):

    def get(self, request, pk):
        category_cost = CategoryCost.objects.get(id=pk)
        form = CategoryCostForm(initial={'name': category_cost.name, 'id': category_cost.id})
        context = {
            'form': form,
            'category_cost':category_cost,
        }
        return render(request, 'costs/category_cost_update.html', context=context)

    def post(self, request, pk):
        category_cost = CategoryCost.objects.get(id=pk)
        b_form = CategoryCostForm(request.POST, initial={'name': category_cost.name, 'id': category_cost.id})
        if b_form.is_valid():
            data = CategoryCostDTO(
                id = category_cost.id,
                name = b_form['name'].value(),
            )
            CategoryCostService(CategoryCostRepository()).update_object(data)
            return redirect('category_costs_list_url')
        context = {
            'form': b_form,
            'category_cost': category_cost,
        }
        return render(request, 'costs/category_cost_create.html', context=context)