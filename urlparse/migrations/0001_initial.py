# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('url', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('encoding', models.CharField(max_length=255)),
                ('h1', models.CharField(max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Url',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('url', models.CharField(max_length=255)),
                ('timeshift', models.TimeField()),
            ],
        ),
    ]
