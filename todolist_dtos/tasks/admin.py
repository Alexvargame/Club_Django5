from django.contrib import admin

from todolist_dtos.models.category import CategoryTask
from todolist_dtos.models.priority import Priority
from todolist_dtos.models.task import Task
from todolist_dtos.models.dayplan import DayPlan

@admin.register(CategoryTask)
class CategoryTaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'name')

@admin.register(Priority)
class PriorityAdmin(admin.ModelAdmin):
    list_display = ('id', 'priority')

@admin.register(Task)
class TaksAdmin(admin.ModelAdmin):
    list_display = (
    'id',
    'user',
    'name',
    'category',
    'description',
    'date_create',
    'date_to_do',
    'priority',
    'status'
    )

@admin.register(DayPlan)
class DayPlanAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'day_date', 'get_tasks')
