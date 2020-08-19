# Generated by Django 3.0.7 on 2020-06-05 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='users',
            field=models.ManyToManyField(blank=True, to='user.User', verbose_name='users'),
        ),
    ]