from django.contrib.auth.models import User

from todolist_dtos.models.cost import Cost
from todolist_dtos.models.category_cost import CategoryCost

from costs.dtos.response.cost_dto import CostDTO

class CostRepository:

    model = Cost

    def list_objects(self):
        return self.model.objects.all()

    def create_object(self, dto):
        cost = self.model.objects.create(
            user=User.objects.get(username=dto.user),
            category=CategoryCost.objects.get(name=dto.category),
            cost_date=dto.cost_date,
            cost_name=dto.cost_name,
            cost_sum=dto.cost_sum
        )
        cost.save()

    def create_many_objects(self, dto_lst):
        for dto in dto_lst:
            cost = self.model.objects.create(
                user=User.objects.get(username=dto.user),
                category=CategoryCost.objects.get(name=dto.category),
                cost_date=dto.cost_date,
                cost_name=dto.cost_name,
                cost_sum=dto.cost_sum
            )
            cost.save()
    def detail_object(self, obj):
        dto = CostDTO(
            id=obj.id,
            user=obj.id,
            category=obj.category,
            cost_date=obj.cost_date,
            cost_name=obj.cost_name,
            cost_sum=obj.cost_sum
        )
        return dto

    def update_object(self, dto):
        cost = self.model.objects.get(id=dto.id)
        for key, value in dto.__dict__.items():
            cost.__dict__[key] = value
        cost.save()

    def delete_object(self, dto):
        obj = self.model.objects.get(id=dto.id)
        print(obj)
        obj.delete()
