from todolist_dtos.models.task import Task

from tasks.dtos.response.task_dto import TaskDTO

class TaskRepository:
    model = Task

    def create_object(self, dto):
        task = self.model.objects.create(
            user=dto.user,
            name=dto.name,
            category=dto.category,
            remark=dto.remark,
            description=dto.description,
            date_create=dto.date_create,
            date_to_do=dto.date_to_do,
            priority=dto.priority,
            status=dto.status
        )
        task.save()

    def list_objects(self):
        return self.model.objects.all()

    def list_for_day_plan(self, user, status, date_b, date_e):
        return self.model.objects.filter(user=user, status=status, date_to_do__range=(date_b, date_e))
    def detail_object(self, obj):
        dto = TaskDTO(
            id=obj.id,
            user=obj.user,
            name=obj.name,
            category=obj.category,
            remark=obj.remark,
            description=obj.description,
            date_create=obj.date_create,
            date_to_do=obj.date_to_do,
            priority=obj.priority,
            status=obj.status
        )
        return dto

    def update_object(self, dto):
        task = self.model.objects.get(id=dto.id)
        for key, value in dto.__dict__.items():
            task.__dict__[key] = value
        task.save()

    def delete_object(self, dto):
        task = self.model.objects.get(id=dto.id)
        task.delete()

    def get_choices_tasks(self, names):
        return self.model.objects.filter(name__in=names)
