from django.db import models
from django.urls import reverse

from .task import Task

class DayPlan(models.Model):
    user=models.CharField(max_length=100, default='admin')
    day_date=models.DateField('День')
    tasks=models.ManyToManyField(Task, verbose_name="задания", related_name="day_tasks", blank=True)


    class Meta:
        verbose_name="Дневной план"
        verbose_name_plural="Дневные планы"

    def get_tasks(self):
        return [task for task in self.tasks.all()]

    def get_absolute_url(self):
        return reverse('day_detail_url',args=[self.day_date.year,self.day_date.month, self.day_date.day, self.user])
