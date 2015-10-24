# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data_registry', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('study_doi', models.CharField(max_length=200)),
                ('individual', models.CharField(max_length=200)),
                ('session', models.CharField(max_length=20)),
                ('url', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Papers',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cite', models.CharField(max_length=1000)),
                ('doi', models.CharField(max_length=200)),
                ('url', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.DeleteModel(
            name='DataFromPapers',
        ),
        migrations.AddField(
            model_name='data',
            name='paper',
            field=models.ManyToManyField(to='data_registry.Papers'),
            preserve_default=True,
        ),
    ]
