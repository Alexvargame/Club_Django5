from dataclasses import dataclass
from typing import List

from todolist_dtos.models.task import Task

@dataclass
class CreateDayPlanDTO:
    user: str
    day_date: str
    tasks: List[Task]
