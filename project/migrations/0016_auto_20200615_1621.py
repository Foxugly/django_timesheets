# Generated by Django 3.0.7 on 2020-06-15 14:21

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0015_auto_20200615_1621'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='close_date',
            field=models.DateField(blank=True, default=django.utils.timezone.now),
        ),
    ]
