from django.contrib import admin

from test_migrate.models.real_estate import RealEstate
from test_migrate.models.flat import Flat
#from estate.models.house import House

@admin.register(RealEstate)
class RealEstateAdmin(admin.ModelAdmin):
    list_display = (
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
        'author',
        'id_object',
        'description',
        'site_link',
        'created_at',
        # 'city',
        # 'district',
        # 'street',
        'number_address_building',
        'number_address_appart',
        'square',
        'price',
        'floor',
        'number_of_storeys',
        'type',
    )

# @admin.register(House)
# class HouseAdmin(admin.ModelAdmin):
#     list_display = (
#         'author',
#         'id_object',
#         'description',
#         'site_link',
#         'created_at',
#         'city',
#         'district',
#         'street',
#         'number_address_building',
#         'number_address_appart',
#         'square',
#         'price',
#         'area',
#         'type',
#     )