from django.db import models
from django.shortcuts import reverse

class CategoryCost(models.Model):

    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Категория расходов"
        verbose_name_plural = "Категории расходов"

    def __str__(self):
        return self.name
