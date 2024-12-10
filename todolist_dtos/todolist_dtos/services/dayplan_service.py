from tasks.dtos.request.create_dayplan_dto import CreateDayPlanDTO


class DayPlanService:

    def __init__(self, repository):
        self.repository = repository

    def create_object(self, dto):
        self.repository.create_object(dto)

    def update_object(self, dto):
        self.repository.update_object(dto)
    def is_exists(self, user, date_b):
        return self.repository.is_exists(user, date_b)

    def get_day(self, user, date_b):
        return self.repository.get_day(user, date_b)

    def detail_object(self, obj):
        return self.repository.detail_object(obj)