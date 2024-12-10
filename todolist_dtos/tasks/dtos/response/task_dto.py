from dataclasses import dataclass

@dataclass
class TaskDTO:
    id: int
    user: str
    name: str
    category: str
    description: str
    remark: str
    date_create: str
    date_to_do: str
    priority: str
    status: bool