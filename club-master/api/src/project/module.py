from injector import Binder, noscope, inject, provider

from .project_service import ProjectService
from .repository import ProjectRepository
from .repository_abc import IProjectRepository

class ProjectServiceModule:
    def configure(self, binder: Binder):
        binder.bind(ProjectRepository, to=ProjectRepository, scope=noscope)

    @provider
    @inject
    def provide_user_service(self, repository):
        return ProjectService(repository)