# Generated by Django 4.2.7 on 2023-11-25 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0004_alter_tasks_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='task_name',
            field=models.CharField(max_length=100),
        ),
    ]
