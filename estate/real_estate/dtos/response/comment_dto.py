from dataclasses import dataclass

@dataclass
class CommentDTO:
    author: str
    real_state: int
    content: str
    created_at: str
    is_active: bool

