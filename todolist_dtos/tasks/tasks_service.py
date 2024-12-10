from .dtos.request.create_task_dto import CreateTaskDTO

class TaskService:

    def __init__(self, repository):
        self.repository = repository

    def create_object(self, dto):
        self.repository.create_object(dto)

    def list_objects(self):
        return self.repository.list_objects()

    def detail_object(self, obj):
        return self.repository.detail_object(obj)

    def update_object(self, dto):
        self.repository.update_object(dto)

    def delete_object(self,dto):
        self.repository.delete_object(dto)

    def list_for_day_plan(self, user, status, date_b, date_e):
        return self.repository.list_for_day_plan(user, status, date_b, date_e)

    def get_choices_tasks(self, names):
        return self.repository.get_choices_tasks(names)