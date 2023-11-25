from rest_framework.serializers import ModelSerializer
from .models import Tasks


class TaskSerializer(ModelSerializer):
    class Meta:
        model = Tasks
        fields = ['task_id', 'task_name', 'status', 'start_date']


class CreateTaskSerializer(ModelSerializer):
    class Meta:
        model = Tasks
        fields = ['task_name', 'start_date']


class UpdateTaskStatusSerializer(ModelSerializer):
    class Meta:
        model = Tasks
        fields = ['status']


class DeleteTaskSerializer(ModelSerializer):
    class Meta:
        model = Tasks
        fields = ['task_id']
