from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status
from .serializers import TaskSerializer, CreateTaskSerializer, UpdateTaskStatusSerializer, DeleteTaskSerializer
from .models import Tasks
from authentication.models import User

from authentication.views import AuthorizeUser


class TaskView(APIView):
    serializer_class = TaskSerializer

    def get(self, request):

        user = AuthorizeUser(request=request)

        tasks = Tasks.objects.filter(owner=user)

        serializer = TaskSerializer(tasks, many=True)

        return Response(serializer.data)


class CreateTask(APIView):
    serializer_class = CreateTaskSerializer

    def post(self, request):

        serializer = TaskSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        user = AuthorizeUser(request=request)

        task_data = {
            'owner': user,
            'task_name': serializer.validated_data['task_name'],
            'start_date': serializer.validated_data.get('start_date'),
        }

        task = Tasks.objects.create(**task_data)

        response_serializer = TaskSerializer(task)

        return Response(response_serializer.data)


class UpdateStatus(APIView):
    serializer_class = UpdateTaskStatusSerializer

    def patch(self, request, task_id):
        user = AuthorizeUser(request=request)

        try:
            task = self.get_object(task_id=task_id, user=user)
        except Tasks.DoesNotExist:
            return Response({'detail': 'Task not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = UpdateTaskStatusSerializer(
            instance=task, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_object(self, task_id, user):
        return Tasks.objects.get(task_id=task_id, owner=user)


class DeleteTask(APIView):
    serializer_class = DeleteTaskSerializer

    def delete(self, request, task_id):
        user = AuthorizeUser(request=request)

        try:
            task = self.get_object(task_id=task_id)
        except Tasks.DoesNotExist:
            return Response({'detail': 'Task not found'}, status=status.HTTP_404_NOT_FOUND)

        task.delete()
        return Response({'detail': 'Task deleted successfully'}, status=status.HTTP_200_OK)

    def get_object(self, task_id):
        return Tasks.objects.get(task_id=task_id)
