from django.db.backends.signals import connection_created
from django.db.backends.postgresql.base import DatabaseWrapper
from django.dispatch import receiver


@receiver(connection_created, sender=DatabaseWrapper)
def initial_connection_to_db(sender, **kwargs):
    from .address import City, District, Street




