# Generated by Django 3.0.7 on 2020-06-08 13:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0004_auto_20200608_1532'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='creation_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]
