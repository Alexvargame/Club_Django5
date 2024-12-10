from dataclasses import dataclass
from typing import List

from todolist_dtos.models.task import Task

@dataclass
class DayPlanDTO:
    id: int
    user: str
    day_date: str
    tasks: List[Task]
