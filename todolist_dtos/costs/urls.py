from django.urls import path

from costs.controllers.category_cost import category_costs

urlpatterns =[
    path('', category_costs.CategoryCostView.as_view(), name='category_costs_list_url'),
]