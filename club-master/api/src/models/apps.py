from django.apps import AppConfig


class ModelsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'src.models'

    def ready(self):
        # from .user import CustomUser
        from .project import Project
        from .category import Category
        from .stack import Stack
        from .vacancy import Vacancy
