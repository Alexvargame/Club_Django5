import json
from django.core.management import BaseCommand

from consultation.models import ServiceModel

class Command(BaseCommand):
    help = 'Load service from json file'

    def handle(self, *args, **options):
        with open('service.json', 'r', encoding='utf-8') as file:
            services = json.load(file)
            for service in services:
                ServiceModel.objects.create(
                    name = service['name'],
                    slug = service['slug'],
                    description = service['decription'],
                    price = service['price'],
                    for_customer = '\n'.join(service['for_customer']),
                    benefit = service['benefit'],
                    features = '\n'.join(service['features']),
                    duration = service['duration'],
                )
        self.stdout.write(self.style.SUCCESS('service loaded successfully'))
