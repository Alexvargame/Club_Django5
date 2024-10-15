from django.db import models



class Street(models.Model):
    name = models.CharField(max_length=100)
    city = models.ForeignKey('City', on_delete=models.DO_NOTHING, related_name='streets')

    def __str__(self):
        return f'{self.city}:{self.name}'
