from django.db import models
from django.urls import reverse
from .real_estate import RealEstate
from .enums import TypeFlat

class Flat(RealEstate):
    def __init__(self, *args, **kwargs):
        super(Flat,self).__init__(*args, **kwargs)
    floor = models.IntegerField(default=1)
    number_of_storeys = models.IntegerField(default=1)
    type = models.CharField(choices=TypeFlat, default=TypeFlat.FLAT, max_length=15)
    rooms = models.IntegerField(default=1)

    class Meta:
        verbose_name = 'Кварира'
        verbose_name_plural = 'Квартиры'
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.type}:{self.id_object}'

    def get_absolute_url(self):
        return reverse('detail_flat', kwargs={'pk': self.id})

    def get_update_url(self):
        return reverse('update_flat', kwargs={'pk': self.id})

    def get_delete_url(self):
        return reverse('delete_flat', kwargs={'pk': self.id})

