# Generated by Django 3.0.7 on 2020-06-10 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timesheet', '0004_auto_20200610_1642'),
    ]

    operations = [
        migrations.AddField(
            model_name='timesheet',
            name='task_done',
            field=models.BooleanField(default=False),
        ),
    ]
