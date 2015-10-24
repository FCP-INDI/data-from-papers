# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data_registry', '0005_auto_20141116_2035'),
    ]

    operations = [
        migrations.AddField(
            model_name='studies',
            name='data_path_template',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='studies',
            name='name',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='data',
            name='scan_type',
            field=models.CharField(max_length=20),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='data',
            name='session',
            field=models.CharField(max_length=20),
            preserve_default=True,
        ),
    ]
