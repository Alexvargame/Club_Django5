from injector import inject

from .repository import ProjectRepository
from .dtos.request.create_project_dto import CreateProjectDTO
from .repository_abc import IProjectRepository

class ProjectService:
    @inject
    def __init__(self, repository: ProjectRepository):
        self.repository = repository# ProjectRepository()

    def create_project(self, dto: CreateProjectDTO) -> None:
        self.repository.create_project(dto)

    def list_projects(self):
        return self.repository.list_projects()

    def get_project(self, pk):
        return self.repository.get_project(pk)