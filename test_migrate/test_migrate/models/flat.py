from django.db import models
#from django.contrib.auth.models import User
from .real_estate import RealEstate
from .enums import TypeFlat

class Flat(RealEstate):
    def __init__(self, *args, **kwargs):
        super(Flat,self).__init__(*args, **kwargs)
    floor = models.IntegerField(default=1)
    number_of_storeys = models.IntegerField(default=1)
    type = models.CharField(choices=TypeFlat, default=TypeFlat.FLAT, max_length=15)

    def __str__(self):
        return f'{self.type}:{self.id_object}'


