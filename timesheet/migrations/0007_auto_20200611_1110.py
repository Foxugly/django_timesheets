# Generated by Django 3.0.7 on 2020-06-11 09:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0007_auto_20200610_1827'),
        ('timesheet', '0006_auto_20200610_1805'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timesheet',
            name='name',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='timesheet',
            name='refer_task',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='back_timesheet_task', to='task.Task', verbose_name='task'),
        ),
    ]
