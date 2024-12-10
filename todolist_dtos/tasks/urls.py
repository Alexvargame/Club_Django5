from django.urls import path
from .controllers.task import create_task, tasks, detail_task, update_task, delete_task
from .controllers.dayplan import create_dayplan, detail_dayplan, update_dayplan, choice_dayplan
from .views import *


urlpatterns = [
    path('', main_menu, name='main_menu_url'),
    path('tasks/', tasks.TasksListvew.as_view(), name='tasks_list_url'),
    path('create/', create_task.TaskCreateView.as_view(), name='task_create_url'),
    path('tasks/<int:pk>/', detail_task.TaskDetailView.as_view(), name='task_detail_url'),
    path('tasks/<int:pk>/update/', update_task.TaskUpdateView.as_view(), name='task_update_url'),
    path('tasks/<int:pk>/delete/', delete_task.TaskDeleteView.as_view(), name='task_delete_url'),

    path('dayplan/create/', create_dayplan.DayPlanCreateView.as_view(), name='day_create_url'),
    path('days/<int:year>/<int:month>/<int:day>/<str:user>/', detail_dayplan.DayPlanDetailView.as_view(),name='day_detail_url'),
    path('days/<int:year>/<int:month>/<int:day>/<str:user>/update/', update_dayplan.DayPlanUpdate.as_view(),name='day_update_url'),
    path('days/', choice_dayplan.ChoiceDayPlanView.as_view(), name='day_choice_url'),
]