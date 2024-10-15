from injector import inject

from django.views import View
from django.shortcuts import render

from src.project.project_service import ProjectService
class ProjectView(View):
    @inject
    def __init__(self, service: ProjectService):
        self.service = service
    def get(self, request):
        projects = self.service.list_projects()
        context = {'projects': projects}#ProjectService().list_projects()}
        return render(request, 'project/list_projects.html', context=context)
