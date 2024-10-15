from django.db import models
from django.urls import reverse
from .real_estate import RealEstate
from .enums import TypeHouse

class House(RealEstate):
    def __init__(self, *args, **kwargs):
        super(House,self).__init__(*args, **kwargs)
    area = models.FloatField()
    type = models.CharField(choices=TypeHouse, default=TypeHouse.HOUSE, max_length=15)
    rooms = models.IntegerField(default=1)

    class Meta:
        verbose_name = 'Дом'
        verbose_name_plural = 'Дома'
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.type}:{self.id_object}'

    def get_absolute_url(self):
        return reverse('detail_house', kwargs={'pk': self.id})

    def get_update_url(self):
        return reverse('update_house', kwargs={'pk': self.id})

    def get_delete_url(self):
        return reverse('delete_house', kwargs={'pk': self.id})


