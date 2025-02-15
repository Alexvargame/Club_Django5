
class DayCostService:

    def __init__(self, repository):
        self.repository = repository

    def detail_object(self, obj):
        return self.repository.detail_object(obj)

    def list_objects(self):
        return self.repository.list_objects()

    def create_object(self, dto):
        self.repository.create_object(dto)
