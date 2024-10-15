from dataclasses import dataclass

@dataclass
class CreateCommentDTO:
    author: str
    real_state: int
    content: str
