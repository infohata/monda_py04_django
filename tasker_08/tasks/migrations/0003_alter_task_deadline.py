# Generated by Django 5.0 on 2024-02-13 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_task_deadline'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='deadline',
            field=models.DateTimeField(blank=True, db_index=True, null=True, verbose_name='deadline'),
        ),
    ]
