from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User



class SearchRequestFlat(models.Model):

    def get_default_cities():
        return dict.fromkeys(['cities'], [])
    def get_default_districts():
        return dict.fromkeys(['districts'], [])
    def get_default_streets():
        return dict.fromkeys(['streets'], [])
    def get_default_types():
        return dict.fromkeys(['types'], [])
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='search_flat_requests')
    created_at = models.DateTimeField(auto_now_add=True)
    square = models.JSONField(blank=True, null=True)
    price = models.JSONField(blank=True, null=True)
    streets = models.JSONField(blank=True, null=True)#(default=get_default_streets, null=True)
    cities = models.JSONField(blank=True, null=True)#default=get_default_cities, null=True)
    districts = models.JSONField(blank=True, null=True)#(default=get_default_districts, null=True)
    rooms = models.JSONField(blank=True, null=True)
    floor = models.JSONField(blank=True, null=True)
    number_of_storeys = models.JSONField(blank=True, null=True)
    type = models.JSONField(blank=True, null=True)#default=get_default_types, null=True)

    def __str__(self):
        return f'{self.author}:{self.type}'


class SearchRequestHouse(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='search_house_requests')
    created_at = models.DateTimeField(auto_now_add=True)
    square = models.JSONField(blank=True, null=True)
    price = models.JSONField(blank=True, null=True)
    streets = models.JSONField(blank=True, null=True)  # (default=get_default_streets, null=True)
    cities = models.JSONField(blank=True, null=True)  # default=get_default_cities, null=True)
    districts = models.JSONField(blank=True, null=True)  # (default=get_default_districts, null=True)
    rooms = models.JSONField(blank=True, null=True)
    area = models.JSONField(blank=True, null=True)
    type = models.JSONField(blank=True, null=True)  # default=get_default_types, null=True)
