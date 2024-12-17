from todolist_dtos.models.category_cost import CategoryCost
from costs.dtos.response.category_cost_dto import CategoryCostDTO

class CategoryCostRepository:

    model = CategoryCost

    def list_objects(self):
        return self.model.objects.all()

    def create_object(self, dto):
        category_cost = self.model.objects.create(name=dto.name)
        category_cost.save()

    def update_object(self, data):
        category_cost = self.model.objects.get(id=data.id)
        for key, value in data.__dict__.items():
            category_cost.__dict__[key] = value
        category_cost.save()

    def detail_object(self, obj):
        dto = CategoryCostDTO(
            id=obj.id,
            name=obj.name,
        )
        return dto

    def delete_object(self, dto):
        obj = self.model.objects.get(id=dto.id)
        obj.delete()