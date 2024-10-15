from django.contrib import admin
from src.models.category import Category
from src.models.stack import Stack
from src.models.vacancy import Vacancy


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name'
    )


@admin.register(Stack)
class StackAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name'
    )

@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    list_display = (
        'project',
        'stack',
        'grade',
        'created_at',
        'updated_at',
        'closed_at',
    )