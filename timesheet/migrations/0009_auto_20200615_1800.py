# Generated by Django 3.0.7 on 2020-06-15 16:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('timesheet', '0008_auto_20200615_1759'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timesheet',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='timesheet',
            name='creation_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
