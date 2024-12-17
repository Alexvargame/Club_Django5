from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin

from todolist_dtos.models.category_cost import CategoryCost
from todolist_dtos.services.category_cost_service import CategoryCostService
from todolist_dtos.repositories.category_cost_repository import CategoryCostRepository

class CategoryCostDetailview(LoginRequiredMixin, View):

    def get(self, request, pk):
        category_cost = CategoryCost.objects.get(id=pk)
        dto = CategoryCostService(CategoryCostRepository()).detail_object(category_cost)
        print('AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAaa',category_cost, dto)
        context ={
            'category_cost': dto.__dict__
        }
        return render(request, 'costs/category_cost_detail.html', context=context)