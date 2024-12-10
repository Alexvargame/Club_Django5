
class CategoryCostService:

    def __init__(self, repository):
        self.repository = repository

    def list_objects(self):
        self.repository.list_objects()