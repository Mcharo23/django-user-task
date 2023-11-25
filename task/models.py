from django.db import models
from enumchoicefield import ChoiceEnum, EnumChoiceField
import uuid

from authentication.models import User


class TaskProgress(ChoiceEnum):
    PENDING = 'pending'
    PROGRESS = 'progress'
    DONE = 'done'


class Tasks(models.Model):
    task_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='tasks')
    task_name = models.CharField(max_length=100)
    status = EnumChoiceField(TaskProgress, default=TaskProgress.PROGRESS)
    start_date = models.DateTimeField(auto_now_add=True)
