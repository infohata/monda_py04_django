# Generated by Django 5.0 on 2024-02-23 08:49

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_project_description_alter_task_description'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='youtube_video_hash',
            field=models.CharField(blank=True, help_text="from Youtube's video URL copy the part after 'https://www.youtube.com/watch?v='.", max_length=50, null=True, verbose_name='YouTube video hash'),
        ),
        migrations.CreateModel(
            name='ProjectLike',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes', to='tasks.project', verbose_name='project')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='project_likes', to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'verbose_name': 'project like',
                'verbose_name_plural': 'project likes',
            },
        ),
    ]
