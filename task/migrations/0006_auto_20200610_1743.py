# Generated by Django 3.0.7 on 2020-06-10 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0005_task_done'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='end_date',
            field=models.DateField(blank=True, null=True, verbose_name='end date'),
        ),
        migrations.AlterField(
            model_name='task',
            name='start_date',
            field=models.DateField(blank=True, null=True, verbose_name='start date'),
        ),
    ]
