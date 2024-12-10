from django.contrib import admin

from todolist_dtos.models.category_cost import CategoryCost
from todolist_dtos.models.cost import Cost

@admin.register(CategoryCost)
class CategoryCostAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(Cost)
class CostAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'category', 'cost_date', 'cost_name', 'cost_sum')
