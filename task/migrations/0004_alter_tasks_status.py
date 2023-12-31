# Generated by Django 4.2.7 on 2023-11-25 18:46

from django.db import migrations
import enumchoicefield.fields
import task.models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0003_alter_tasks_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='status',
            field=enumchoicefield.fields.EnumChoiceField(default=task.models.TaskProgress(2), enum_class=task.models.TaskProgress, max_length=8),
        ),
    ]
