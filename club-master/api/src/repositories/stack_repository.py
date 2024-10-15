from src.models.stack import Stack

class StackRepository:
    model = Stack

    def list_stacks(self):
        return self.model.objects.all()