# Generated by Django 3.0.7 on 2020-06-09 12:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('client', '0007_auto_20200609_1404'),
        ('project', '0007_auto_20200609_1404'),
        ('user', '0003_auto_20200608_1605'),
        ('tag', '0003_auto_20200608_1605'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=20, null=True, verbose_name='name')),
                ('duration', models.DurationField(verbose_name='estimated duration')),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('refer_client', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='back_task_client', to='client.Client', verbose_name='client')),
                ('refer_project', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='back_task_project', to='project.Project', verbose_name='project')),
                ('tags', models.ManyToManyField(blank=True, to='tag.Tag', verbose_name='tags')),
                ('users', models.ManyToManyField(blank=True, to='user.User', verbose_name='users')),
            ],
            options={
                'verbose_name': 'task',
                'verbose_name_plural': 'tasks',
                'ordering': ('name',),
            },
        ),
    ]