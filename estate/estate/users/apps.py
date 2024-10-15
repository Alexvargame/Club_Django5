from django.apps import AppConfig


class UsersConfig(AppConfig):
    #default_auto_field = 'django.db.models.BigAutoField'
    name = 'estate.users'

    def ready(self):
       import estate.users.signals
       #from .models import Profile, PhoneNumber

