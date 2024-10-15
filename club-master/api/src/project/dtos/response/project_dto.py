from ninja import Schema

class ProjectDTO(Schema):
    id: int
    name: str
    description: str
    repo_link: str
    status: str
    author_role: str
    deadline: str
    author_id: int
    categories: list
    stacks: list