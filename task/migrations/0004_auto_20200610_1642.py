# Generated by Django 3.0.7 on 2020-06-10 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timesheet', '0003_auto_20200605_1924'),
        ('task', '0003_auto_20200609_1505'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='end_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='end date'),
        ),
        migrations.AddField(
            model_name='task',
            name='start_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='start date'),
        ),
        migrations.AddField(
            model_name='task',
            name='timesheets',
            field=models.ManyToManyField(blank=True, to='timesheet.Timesheet', verbose_name='timesheets'),
        ),
    ]