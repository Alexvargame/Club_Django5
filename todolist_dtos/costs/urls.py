from django.urls import path

from costs.controllers.category_cost import (
    category_costs,
    create_category_cost,
    update_category_cost,
    detail_category_cost,
    delete_category_cost,
)
from costs.controllers.costs import (
    costs,
    create_cost,
    detail_cost,
    update_cost,
    delete_cost,
    create_many_cost,
)

urlpatterns =[
    path('category_costs/', category_costs.CategoryCostView.as_view(), name='category_costs_list_url'),
    path('category_costs/create/',create_category_cost.CategoryCostCreateView.as_view(),
         name='category_cost_create_url'),
    path('category_costs/<int:pk>/', detail_category_cost.CategoryCostDetailview.as_view(),
         name='category_cost_detail_url'),
    path('category_costs/<int:pk>/update/',update_category_cost.CategoryCostUpdateView.as_view(),
         name='category_cost_update_url'),
    path('category_costs/<int:pk>/delete/',delete_category_cost.CategoryCostDeleteView.as_view(),
         name='category_cost_delete_url'),

    path('costs/', costs.CostslistView.as_view(), name='costs_list_url'),
    path('costs/create/', create_cost.CostCreateView.as_view(), name='cost_create_url'),
    path('costs/create_many/', create_many_cost.CostManyCreateView.as_view(), name='cost_many_create_url'),
    path('costs/<int:pk>/', detail_cost.CostDetailView.as_view(), name='cost_detail_url'),
    path('costs/<int:pk>/update/', update_cost.CostUpdateView.as_view(), name='cost_update_url'),
    path('costs/<int:pk>/delete/',delete_cost.CostDeleteview.as_view(), name='cost_delete_url'),


]