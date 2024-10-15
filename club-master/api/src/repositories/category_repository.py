from src.models.category import Category

class CategoryRepository:
    model = Category

    def list_categories(self):
        return self.model.objects.all()