# Generated by Django 3.0.7 on 2020-06-11 17:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0010_project_timesheets'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='end_date',
            field=models.DateField(default=datetime.datetime(2020, 6, 11, 19, 44, 55, 92938)),
        ),
        migrations.AddField(
            model_name='project',
            name='start_date',
            field=models.DateField(default=datetime.datetime(2020, 6, 11, 19, 44, 55, 92917)),
        ),
    ]