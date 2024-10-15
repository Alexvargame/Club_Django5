from django.db import models
from django.contrib.auth.models import User


class City(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
class Region(models.Model):
    name = models.CharField(max_length=100)
    city = models.ForeignKey(City, on_delete=models.DO_NOTHING, related_name='regi')


class District(models.Model):
    name = models.CharField(max_length=100)
    city = models.ForeignKey(City, on_delete=models.DO_NOTHING, related_name='districts')

    def __str__(self):
        return f'{self.city}:{self.name}'

class Street(models.Model):
    name = models.CharField(max_length=100)
    city = models.ForeignKey(City, on_delete=models.DO_NOTHING, related_name='streets')

    def __str__(self):
        return f'{self.city}:{self.name}'



class RealEstate(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='real_estates')
    id_object = models.CharField(max_length=100)
    description = models.TextField(max_length=5000, blank=True, null=True)
    site_link = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    square = models.FloatField(default=1.0)
    price = models.DecimalField(default=1.00, max_digits=10, decimal_places=2)
    # city = models.CharField(max_length=100, choices=[(str(city.id), city.name) for city in City.objects.all()])
    #district = models.CharField(max_length=100, choices=[(str(dist.id), f'{dist.city}:{dist.name}') for dist in District.objects.all()])
    # street = models.CharField(max_length=100, choices=[(str(st.id), f'{st.city}:{st.name}') for st in Street.objects.all()])
    #city = models.ForeignKey(City, on_delete=models.DO_NOTHING, related_name='real_estates'),
    district = models.ForeignKey(District, on_delete=models.DO_NOTHING, related_name='real_estates', default=1)
    #street = models.ForeignKey('Street', on_delete=models.DO_NOTHING, related_name='real_estates', default=1),

    number_address_building = models.CharField(max_length=5, default=1)
    number_address_appart = models.CharField(max_length=5, default=1)
    city = models.ForeignKey(City, on_delete=models.DO_NOTHING, related_name='real_estates')
    street = models.ForeignKey(Street, on_delete=models.DO_NOTHING, related_name='real_estates')
