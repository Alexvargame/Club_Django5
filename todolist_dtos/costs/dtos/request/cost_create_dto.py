from dataclasses import dataclass

from django.contrib.auth.models import User
from todolist_dtos.models.cost import Cost

@dataclass
class CostCreateDTO:
    user: str
    category: str
    cost_date: str
    cost_name: str
    cost_sum: float