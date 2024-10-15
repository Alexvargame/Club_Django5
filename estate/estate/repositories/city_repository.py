from estate.models.city import City

class CityRepository:
    model = City

    def list_cities(self):
        return self.model.objects.all()

    def filter_cities(self, data):
        return self.model.objects.filter(id__in=data)