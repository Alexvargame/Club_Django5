from django.urls import path

from .views import *

urlpatterns = [
    path('', ProjectView.as_view(), name='list_project'),
    path('create/', ProjectCreateView.as_view(), name='create_project'),
]
