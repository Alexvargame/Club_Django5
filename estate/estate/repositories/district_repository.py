from estate.models.district import District

class DistrictRepository:
    model = District

    def list_districts(self):
        return self.model.objects.all()

    def filter_districts(self, lst):
        return self.model.objects.filter(id__in=lst)