# Generated by Django 3.0.7 on 2020-06-05 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
        ('client', '0001_initial'),
        ('tag', '0001_initial'),
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='projects',
            field=models.ManyToManyField(blank=True, to='project.Project', verbose_name='projects'),
        ),
        migrations.AddField(
            model_name='client',
            name='tags',
            field=models.ManyToManyField(blank=True, to='tag.Tag', verbose_name='tags'),
        ),
        migrations.AddField(
            model_name='client',
            name='users',
            field=models.ManyToManyField(blank=True, to='user.User', verbose_name='users'),
        ),
    ]
