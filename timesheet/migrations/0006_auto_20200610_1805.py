# Generated by Django 3.0.7 on 2020-06-10 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_user_color'),
        ('timesheet', '0005_timesheet_task_done'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='timesheet',
            name='user',
        ),
        migrations.AddField(
            model_name='timesheet',
            name='users',
            field=models.ManyToManyField(blank=True, to='user.User', verbose_name='user'),
        ),
    ]
