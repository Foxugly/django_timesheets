# Generated by Django 3.0.7 on 2020-06-08 14:05

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tag', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='tag',
            name='creation_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]
