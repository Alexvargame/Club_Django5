from estate.models.street import Street

class StreetRepository:
    model = Street

    def list_streets(self):
        return self.model.objects.all()

    def filter_streets(self, lst):
        return self.model.objects.filter(id__in=lst)