# Generated by Django 3.0.7 on 2020-06-05 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timesheet', '0002_auto_20200605_1909'),
        ('customuser', '0002_auto_20200605_1815'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='timesheets',
            field=models.ManyToManyField(blank=True, to='timesheet.Timesheet', verbose_name='timesheets'),
        ),
    ]
