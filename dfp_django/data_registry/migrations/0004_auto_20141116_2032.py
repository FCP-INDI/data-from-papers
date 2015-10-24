# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data_registry', '0003_auto_20141115_2339'),
    ]

    operations = [
        migrations.CreateModel(
            name='Study',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('doi', models.CharField(unique=True, max_length=200)),
                ('description', models.TextField()),
                ('url', models.URLField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='data',
            name='study_doi',
        ),
        migrations.AddField(
            model_name='data',
            name='study',
            field=models.ForeignKey(default=1, to='data_registry.Study'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='papers',
            name='doi',
            field=models.CharField(unique=True, max_length=200),
            preserve_default=True,
        ),
    ]
