from django.db import models

class CategoryTask(models.Model):
    user=models.CharField(max_length=100, default='admin')
    name=models.CharField(max_length=100)

    class Meta:
        verbose_name='Категория задания'
        verbose_name_plural='Категории заданий'

    def __str__(self):

        return f"{self.name}"