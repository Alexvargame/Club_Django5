from django.db import models
from django.urls import reverse


from todolist_dtos.models.cost import Cost
class DayCost(models.Model):
    user = models.CharField(verbose_name='Пользователь', max_length=100, default='admin')
    day_date = models.DateField(verbose_name='День')
    costs = models.ManyToManyField(Cost, verbose_name="Расходы", related_name="day_costs", blank=True)

    class Meta:
        verbose_name = "Дневной расход"
        verbose_name_plural = "Дневные расходы"

    def get_absolute_url(self):
        return reverse('day_cost_detail_url',
                       args=[self.day_date.year, self.day_date.month, self.day_date.day, self.user])

    # def get_update_url(self):
    #     return reverse('day_cost_update_url',
    #                    args=[self.day_date.year, self.day_date.month, self.day_date.day, self.user])

    def get_costs(self):
        costs_dict = {}
        for cost in self.costs.all():
            key, value = cost.cost_name, cost.cost_sum
            costs_dict[key] = value

        return costs_dict

    def get_day_sum(self):
        return sum(self.get_costs().values())