# Generated by Django 3.0.7 on 2020-06-08 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0003_auto_20200608_1531'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='creation_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
