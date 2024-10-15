from django.contrib import admin
from .models import RealEstate, Street, City, District


@admin.register(RealEstate)
class RealEstateAdmin(admin.ModelAdmin):
    list_display = (
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
        'price',
    )

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name'
    )


@admin.register(District)
class DisctrictAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'city',
    )

@admin.register(Street)
class StreetAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'city',
    )


