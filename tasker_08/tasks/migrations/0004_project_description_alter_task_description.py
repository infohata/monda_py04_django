# Generated by Django 5.0 on 2024-02-18 08:22

import tinymce.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_alter_task_deadline'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='description',
            field=tinymce.models.HTMLField(blank=True, max_length=10000, null=True, verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='task',
            name='description',
            field=tinymce.models.HTMLField(blank=True, max_length=10000, null=True, verbose_name='description'),
        ),
    ]
