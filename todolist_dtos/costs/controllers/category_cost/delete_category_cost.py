from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin


from todolist_dtos.services.category_cost_service import CategoryCostService
from todolist_dtos.repositories.category_cost_repository import CategoryCostRepository
from todolist_dtos.models.category_cost import CategoryCost
from costs.dtos.response.category_cost_dto import CategoryCostDTO
#from costs.forms import CategoryCostForm

class CategoryCostDeleteView(LoginRequiredMixin, View):

    def get(self, request, pk):
        category_cost = CategoryCost.objects.get(id=pk)
        context = {
            'category_cost': category_cost,
        }
        return render(request, 'costs/category_cost_delete.html', context=context)

    def post(self, request, pk):
        category_cost = CategoryCost.objects.get(id=pk)
        dto = CategoryCostDTO(
            name=category_cost.name,
            id=category_cost.id
        )
        CategoryCostService(CategoryCostRepository()).delete_object(dto)
        return redirect('category_costs_list_url')