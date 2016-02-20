# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('urlparse', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='timeshift',
            field=models.TimeField(default='00:00:00'),
        ),
    ]
