from django.contrib import admin

from estate.models.real_estate import RealEstate
from estate.models.flat import Flat
from estate.models.house import House

@admin.register(RealEstate)
class RealEstateAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'author',
        'id_object',
        'description',
        'site_link',
        'created_at',
        #'city',
        #'district',
        #'street',
        'number_address_building',
        'number_address_appart',
        'square',
        'price',

    )

@admin.register(Flat)
class FlatAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'author',
        'id_object',
        'description',
        'site_link',
        'created_at',
        'city',
        'district',
        'street',
        'number_address_building',
        'number_address_appart',
        'square',
        'rooms',
        'price',
        'floor',
        'number_of_storeys',
        'type',
    )

@admin.register(House)
class HouseAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'author',
        'id_object',
        'description',
        'site_link',
        'created_at',
        'city',
        'district',
        'street',
        'number_address_building',
        'number_address_appart',
        'square',
        'rooms',
        'price',
        'area',
        'type',
    )