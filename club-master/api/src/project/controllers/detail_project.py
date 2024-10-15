from injector import inject

from django.views import View
from django.shortcuts import render

from src.project.project_service import ProjectService


class DetailProjectView(View):
    @inject
    def __init__(self, servive: ProjectService):
        self.service = servive
    def get(self, request, pk):
        project = self.service.get_project(pk)
        #project = ProjectService().get_project(pk)
        context = {'project': project}
        return render(request, 'project/detail_projects.html', context=context)
