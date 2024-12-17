
class CategoryCostService:

    def __init__(self, repository):
        self.repository = repository

    def list_objects(self):
        return self.repository.list_objects()

    def create_object(self, dto):
        self.repository.create_object(dto)

    def update_object(self, dto):
        self.repository.update_object(dto)

    def detail_object(self, obj):
        return self.repository.detail_object(obj)

    def delete_object(self, dto):
        self.repository.delete_object(dto)