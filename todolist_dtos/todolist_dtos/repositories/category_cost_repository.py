from todolist_dtos.models.category_cost import CategoryCost

class CategoryCostRepository:

    model = CategoryCost

    def list_objects(self):
        return self.model.objects.all()