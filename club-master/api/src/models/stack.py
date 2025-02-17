from django.db import models


class Stack(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.name