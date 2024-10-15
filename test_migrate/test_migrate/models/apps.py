from django.apps import AppConfig


class ModelsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'test_migrate.models'
    #
    def ready(self):
        # from .user import CustomUser
        from .real_estate import RealEstate
        #from .signals import initial_connection_to_db
        #from .address import City, District, Street
        from .street import Street
        from .district import  District
        from .city import City
        #
        #

