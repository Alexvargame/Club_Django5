from django.contrib import admin

from .models import Project, Category, Stack

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'status',
        'author_role',
        'created_at',
        'deadline',
        'closed_at',
        'author',
        'get_categories',
        'get_stacks',
    )

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