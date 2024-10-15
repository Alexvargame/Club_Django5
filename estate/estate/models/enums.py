from django.db import models


# class Status(models.TextChoices):
#     OPEN = "OPEN", "Открыт"
#     CLOSED = "CLOSED", "Закрыт"
#     STARTED = "STARTED", "Стартовал"
#     BACKLOG = "BACKLOG", "Backlog"


class TypeHouse(models.TextChoices):
    HOUSE = "HOUSE", "House"
    HARF_HOUSE = "HARF_HOUSE", "Harf_house"


class TypeFlat(models.TextChoices):
    FLAT = "FLAT", "Flat"
    SMART_FLAT = "SMART_FLAT", "Smart_flat"