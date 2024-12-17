from django.views import View
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin


from todolist_dtos.services.category_cost_service import CategoryCostService
from todolist_dtos.repositories.category_cost_repository import CategoryCostRepository

class CategoryCostView(LoginRequiredMixin, View):

    def get(self, request):
        context = {
            'categorycosts': CategoryCostService(CategoryCostRepository()).list_objects()
        }
        print(context)
        return render(request, 'costs/category_cost_list.html', context=context)