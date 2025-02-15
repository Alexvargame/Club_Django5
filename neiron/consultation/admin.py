from django.contrib import admin

from .models import ServiceModel, ClientRequest

@admin.register(ServiceModel)
class ServiceModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug', 'price', 'description',
                    'for_customer', 'benefit', 'features', 'duration')

@admin.register(ClientRequest)
class ClientRequest(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'telegram', 'service', 'message', 'created_at')