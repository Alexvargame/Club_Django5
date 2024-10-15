from django.apps import AppConfig


class ModelsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'estate.models'

    def ready(self):
        from .real_estate import RealEstate
        from .city import City
        from .street import Street
        from .district import  District
        from .search_requests import SearchRequestFlat
        from .comments import Comment
        from .profile import Profile, PhoneNumber


