from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    avatar = models.CharField(max_length=255, null=True)
    telegram = models.CharField(max_length=255, null=True)
