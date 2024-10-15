from src.models.project import Project
from .repository_abc import IProjectRepository

class ProjectRepository:#(IProjectRepository):
    model = Project

    def create_project(self, dto):
        project = self.model.objects.create(
            name=dto.name,
            description=dto.description,
            repo_link=dto.repo_link,
            status=dto.status,
            author_role=dto.author_role,
            deadline=dto.deadline,
            author_id=dto.author_id
        )
        project.categories.add(*dto.categories)
        project.stacks.add(*dto.stacks)
        project.save()

    def list_projects(self):
        return self.model.objects.all()

    def get_project(self, pk):
        return self.model.objects.prefetch_related('categories', 'stacks').get(id=pk)