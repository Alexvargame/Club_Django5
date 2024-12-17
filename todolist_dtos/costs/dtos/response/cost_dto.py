from dataclasses import dataclass
from django.contrib.auth.models import User

from todolist_dtos.models.cost import Cost
from todolist_dtos.models.category_cost import CategoryCost
@dataclass
class CostDTO:
    id: int
    user: User
    category: CategoryCost
    cost_date: str
    cost_name: str
    cost_sum: float


