# Generated by Django 3.0.7 on 2020-06-15 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0008_task_close_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='close_date',
            field=models.DateField(blank=True, null=True, verbose_name='close date'),
        ),
    ]
