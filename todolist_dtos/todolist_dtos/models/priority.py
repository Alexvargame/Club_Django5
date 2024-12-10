from django.db import models

class Priority(models.Model):
    priority=models.CharField('Приоритет',max_length=30)

    class Meta:
        verbose_name='Приоритет'
        verbose_name_plural='Приоритеты'

    def __str__(self):
        return self.priority
