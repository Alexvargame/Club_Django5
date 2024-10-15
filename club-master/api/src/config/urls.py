
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

from ninja_extra import NinjaExtraAPI
from src.project.api import ProjectController


api = NinjaExtraAPI()

#api.add_router('project/', 'src.project.api.router')

api.register_controllers(ProjectController)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/", include("src.account.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
    path("project/", include("src.project.urls")),
    path('api/', api.urls),
    path("", TemplateView.as_view(template_name="home.html"), name="home"),
]
urlpatterns+=[path('silk/', include('silk.urls', namespace='silk'))]

