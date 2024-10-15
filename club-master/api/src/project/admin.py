from django.contrib import admin
from src.models.project import Project


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

