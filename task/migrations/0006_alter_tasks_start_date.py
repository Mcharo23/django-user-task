# Generated by Django 5.0.2 on 2024-02-26 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0005_alter_tasks_task_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='start_date',
            field=models.DateTimeField(),
        ),
    ]