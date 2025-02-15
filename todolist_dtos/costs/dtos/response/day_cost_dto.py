from dataclasses import dataclass
from typing import List

from todolist_dtos.models.cost import Cost
from django.contrib.auth.models import User

@dataclass
class DayCostDTO:

    id: int
    user: User
    day_date: str
    costs: List[Cost]

