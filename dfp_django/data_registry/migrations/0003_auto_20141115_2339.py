# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data_registry', '0002_auto_20141115_0953'),
    ]

    operations = [
        migrations.AddField(
            model_name='data',
            name='scan_type',
            field=models.CharField(default=b'anat', max_length=20),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='data',
            name='session',
            field=models.CharField(default=b'1', max_length=20),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='data',
            name='url',
            field=models.URLField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='papers',
            name='cite',
            field=models.TextField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='papers',
            name='url',
            field=models.URLField(),
            preserve_default=True,
        ),
    ]
