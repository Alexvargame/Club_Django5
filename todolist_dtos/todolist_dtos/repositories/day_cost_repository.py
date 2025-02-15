from todolist_dtos.models.day_cost import DayCost

from costs.dtos.response.day_cost_dto import DayCostDTO

class DayCostRepository:

    model = DayCost

    def detail_object(self, obj):
        dto = DayCostDTO(
            id=obj.id,
            user=obj.user,
            day_date=obj.day_date,
            costs=obj.costs
        )
        return dto

    def list_objects(self):
        return self.model.objects.all()

    def create_object(self, dto):
        day_cost = self.model.objects.create(
            user=dto.user,
            day_date=dto.day_date,
        )
        day_cost.costs.set(dto.costs)
        day_cost.save()
