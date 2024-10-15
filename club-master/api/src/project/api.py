from typing import List

from ninja_extra import api_controller, route, ControllerBase
from .dtos.response.project_dto import ProjectDTO
from injector import inject
from .project_service import ProjectService


#router = Router()
@api_controller('/project')
class ProjectController(ControllerBase):
    def __init__(self, service: ProjectService):
        self.service = service
    @route.get('/', response=List[ProjectDTO])
    def list_projects(self):
        return self.service.list_projects()

# @router.get('/', response=List[ProjectDTO])
# @inject
# def list_projects(request, service: ProjectService):
#     return service.list_projects()