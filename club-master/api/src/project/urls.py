from django.urls import path
from .controllers import list_projects, create_project, detail_project

#from .api import api
urlpatterns = [
    path('create/', create_project.ProjectCreateView.as_view(), name="create_project"),
    path('', list_projects.ProjectView.as_view(), name="list_project"),
    path('<int:pk>/', detail_project.DetailProjectView.as_view(), name='detail_project'),
]
