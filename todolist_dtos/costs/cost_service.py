class CostService:

    def __init__(self, repository):
        self.repository = repository

    def list_objects(self):
        return self.repository.list_objects()

    def create_object(self, dto):
        self.repository.create_object(dto)

    def create_many_objects(self, dto_lst):
        self.repository.create_many_objects(dto_lst)
    def detail_object(self, obj):
        return self.repository.detail_object(obj)

    def update_object(self, dto):
        self.repository.update_object(dto)

    def delete_object(self, dto):
        self.repository.delete_object(dto)