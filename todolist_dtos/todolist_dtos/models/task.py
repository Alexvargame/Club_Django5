from django.db import models
from django.urls import reverse

class Task(models.Model):
    user = models.CharField(max_length=100, default='')
    name = models.CharField('Название', max_length=100)
    category = models.CharField('Категория', max_length=30, blank=True, null=True)
    description = models.CharField('Описание', max_length=2500)
    remark = models.CharField('Примечания', max_length=2500, default='', blank=True)
    date_create = models.DateTimeField('Дата создания')
    date_to_do = models.DateTimeField('Дата исполнения')
    priority = models.CharField('Приоритет', max_length=30)
    status = models.BooleanField("Статус исполнения", default=False)

    class Meta:
        verbose_name = 'Задание'
        verbose_name_plural = 'Задания'

    def __str__(self):
        return f"{self.user}-{self.name}"

    def get_absolute_url(self):
        return reverse('task_detail_url', kwargs={'pk': self.id})

    def get_update_url(self):
        return reverse('task_update_url', kwargs={'pk': self.id})
