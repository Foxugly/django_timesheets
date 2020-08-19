# Generated by Django 3.0.7 on 2020-06-05 15:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('client', '0001_initial'),
        ('tag', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='name')),
                ('description', models.CharField(max_length=300, verbose_name='description')),
                ('refer_client', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='back_project_client', to='client.Client', verbose_name='client')),
                ('tags', models.ManyToManyField(blank=True, to='tag.Tag', verbose_name='tags')),
            ],
            options={
                'verbose_name': 'projet',
                'verbose_name_plural': 'projects',
                'ordering': ('name',),
            },
        ),
    ]