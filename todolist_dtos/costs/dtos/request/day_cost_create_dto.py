from dataclasses import dataclass
from typing import List

from todolist_dtos.models.cost import Cost
@dataclass
class DayCostCreateDTO:
    user: str
    day_date: str
    costs: List[Cost]
