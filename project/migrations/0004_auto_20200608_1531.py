# Generated by Django 3.0.7 on 2020-06-08 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0003_auto_20200605_1923'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='description'),
        ),
    ]
