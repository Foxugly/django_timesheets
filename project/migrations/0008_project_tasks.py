# Generated by Django 3.0.7 on 2020-06-10 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0003_auto_20200609_1505'),
        ('project', '0007_auto_20200609_1404'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='tasks',
            field=models.ManyToManyField(blank=True, to='task.Task', verbose_name='tasks'),
        ),
    ]
