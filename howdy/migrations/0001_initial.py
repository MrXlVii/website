# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-06 06:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter the project language', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('summary', models.TextField(help_text='Enter a brief description of the project', max_length=1000)),
                ('version', models.CharField(help_text='(max) 12 Character version number e.g. 1.0.1 or in progress', max_length=8, verbose_name='Version')),
                ('language', models.ManyToManyField(help_text='Select the language for this project', to='howdy.Language')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectInstance',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='Unique ID for this particular project', primary_key=True, serialize=False)),
                ('imprint', models.CharField(max_length=200)),
                ('last_update', models.DateField(blank=True, null=True)),
                ('status', models.CharField(blank=True, choices=[('e', 'Early Phases'), ('a', 'Alpha'), ('b', 'Beta'), ('c', 'Completed/Released')], default='e', help_text='Project status', max_length=1)),
                ('project', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='howdy.Project')),
            ],
            options={
                'ordering': ['last_update'],
            },
        ),
    ]
