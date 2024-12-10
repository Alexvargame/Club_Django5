from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import reverse
from todolist_dtos.models.category_cost import CategoryCost

class Cost(models.Model):
    user = models.ForeignKey(User, related_name='cost_creator', on_delete=models.DO_NOTHING, null=True, blank=True)
    category = models.ForeignKey(CategoryCost, related_name='category_cost', on_delete=models.DO_NOTHING, null=True, blank=True)
    cost_date = models.DateField()
    cost_name = models.CharField(max_length=1000, blank=True)
    cost_sum = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = "Расход"
        verbose_name_plural = "Расходы"
