from django.urls import path
from .views import TaskView, CreateTask, UpdateStatus, DeleteTask

urlpatterns = [
    path('', TaskView.as_view(), name='tasks'),
    path('create-task/', CreateTask.as_view(), name='create-task'),
    path('update-status/<uuid:task_id>/',
         UpdateStatus.as_view(), name='update-status'),
    path('delete-task/<uuid:task_id>/', DeleteTask.as_view(), name='delete-task'),
]
