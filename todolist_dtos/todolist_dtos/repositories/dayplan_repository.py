from todolist_dtos.models.dayplan import DayPlan

from tasks.dtos.response.dayplan_dto import DayPlanDTO

from datetime import date
class DayPlanRepository:
    model = DayPlan

    def is_exists(self, user, date_b):
        if self.model.objects.filter(user=user, day_date=date(date_b[0],date_b[1],date_b[2])).exists():
            return True
        return False

    def get_day(self, user, date_b):
        return self.model.objects.get(user=user, day_date=date(date_b[0],date_b[1],date_b[2]))

    def create_object(self, dto):
        dayplan = self.model.objects.create(
            user=dto.user,
            day_date=dto.day_date,
        )
        dayplan.tasks.set(dto.tasks)
        dayplan.save()

    def update_object(self, dto):

        dayplan = self.model.objects.update_or_create(
            user=dto.user,
            day_date=dto.day_date,
        )
        dayplan[0].tasks.set(dto.tasks)
        dayplan[0].save()


    def detail_object(self, obj):
        dto = DayPlanDTO(
            id=obj.id,
            user=obj.user,
            day_date=obj.day_date,
            tasks=obj.tasks,
        )
        return dto