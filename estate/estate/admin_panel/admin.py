from django.contrib import admin
#from estate.models.address import Street, City, District
from estate.models.city import City
from estate.models.district import District
from estate.models.street import Street
from estate.models.search_requests import SearchRequestFlat, SearchRequestHouse
from estate.models.comments import Comment
from estate.models.profile import Profile, PhoneNumber

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

@admin.register(SearchRequestFlat)
class SearchRequestFlatAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'type',
        'cities',
        'districts',
        'streets',
        'floor',
        'number_of_storeys',
        'square',
        'price'
    )

@admin.register(SearchRequestHouse)
class SearchRequestHouseAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'type',
        'cities',
        'districts',
        'streets',
        'area',
        'square',
        'price'
    )
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'real_state',
        'author',
        'content',
        'is_active',
        'created_at',
    )


@admin.register(PhoneNumber)
class PhoneNumberAdmin(admin.ModelAdmin):
    list_display=('phone_number',)

admin.site.register(Profile)
